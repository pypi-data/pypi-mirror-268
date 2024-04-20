import threading
import time

import numpy as np
from bec_lib import bec_logger
from ophyd import Component as Cpt
from ophyd import Device, PositionerBase, Signal
from ophyd.status import wait as status_wait
from ophyd.utils import LimitError

from ophyd_devices.galil.galil_ophyd import (
    BECConfigError,
    GalilAxesReferenced,
    GalilController,
    GalilError,
    GalilMotorIsMoving,
    GalilMotorResolution,
    GalilSetpointSignal,
    GalilSignalRO,
    retry_once,
)
from ophyd_devices.utils.controller import threadlocked
from ophyd_devices.utils.socket import SocketIO, raise_if_disconnected

logger = bec_logger.logger


class FlomniGalilController(GalilController):
    USER_ACCESS = [
        "describe",
        "show_running_threads",
        "galil_show_all",
        "socket_put_and_receive",
        "socket_put_confirmed",
        "drive_axis_to_limit",
        "find_reference",
        "get_motor_limit_switch",
        "fosaz_light_curtain_is_triggered",
        "is_motor_on",
        "all_axes_referenced",
        "lights_off",
        "lights_on",
    ]

    def is_axis_moving(self, axis_Id, axis_Id_numeric) -> bool:
        if axis_Id is None and axis_Id_numeric is not None:
            axis_Id = self.axis_Id_numeric_to_alpha(axis_Id_numeric)
        active_thread = self.is_thread_active(0)
        motor_is_on = self.is_motor_on(axis_Id)
        return bool(active_thread or motor_is_on)

    def all_axes_referenced(self) -> bool:
        # TODO: check if all axes are referenced in all controllers
        return super().all_axes_referenced()

    def fosaz_light_curtain_is_triggered(self) -> bool:
        """
        Check the light curtain status for fosaz

        Returns:
            bool: True if the light curtain is triggered
        """

        return int(float(self.socket_put_and_receive("MG @IN[14]").strip())) == 1

    def lights_off(self) -> None:
        """
        Turn off the lights
        """
        self.socket_put_confirmed("CB15")

    def lights_on(self) -> None:
        """
        Turn on the lights
        """
        self.socket_put_confirmed("SB15")


class FlomniGalilReadbackSignal(GalilSignalRO):
    @retry_once
    @threadlocked
    def _socket_get(self) -> float:
        """Get command for the readback signal

        Returns:
            float: Readback value after adjusting for sign and motor resolution.
        """

        current_pos = float(self.controller.socket_put_and_receive(f"TD{self.parent.axis_Id}"))
        current_pos *= self.parent.sign
        step_mm = self.parent.motor_resolution.get()
        return current_pos / step_mm

    def read(self):
        self._metadata["timestamp"] = time.time()
        val = super().read()
        return val


class FlomniGalilSetpointSignal(GalilSetpointSignal):
    @retry_once
    @threadlocked
    def _socket_set(self, val: float) -> None:
        """Set a new target value / setpoint value. Before submission, the target value is adjusted for the axis' sign.
        Furthermore, it is ensured that all axes are referenced before a new setpoint is submitted.

        Args:
            val (float): Target value / setpoint value

        Raises:
            GalilError: Raised if not all axes are referenced.

        """
        target_val = val * self.parent.sign
        self.setpoint = target_val
        axes_referenced = self.controller.all_axes_referenced()
        if axes_referenced:
            while self.controller.is_thread_active(0):
                time.sleep(0.1)

            self.controller.socket_put_confirmed(f"naxis={self.parent.axis_Id_numeric}")
            self.controller.socket_put_confirmed(f"ntarget={target_val:.3f}")
            self.controller.socket_put_confirmed("movereq=1")
            self.controller.socket_put_confirmed("XQ#NEWPAR")
            while self.controller.is_thread_active(0):
                time.sleep(0.005)
        else:
            raise GalilError("Not all axes are referenced.")


class FlomniGalilMotorResolution(GalilMotorResolution):
    pass


class FlomniGalilMotorIsMoving(GalilMotorIsMoving):
    pass


class FlomniGalilAxesReferenced(GalilAxesReferenced):
    pass


class FlomniGalilMotor(Device, PositionerBase):
    USER_ACCESS = ["controller"]
    readback = Cpt(FlomniGalilReadbackSignal, signal_name="readback", kind="hinted")
    user_setpoint = Cpt(FlomniGalilSetpointSignal, signal_name="setpoint")
    motor_resolution = Cpt(FlomniGalilMotorResolution, signal_name="resolution", kind="config")
    motor_is_moving = Cpt(FlomniGalilMotorIsMoving, signal_name="motor_is_moving", kind="normal")
    all_axes_referenced = Cpt(
        FlomniGalilAxesReferenced, signal_name="all_axes_referenced", kind="config"
    )
    high_limit_travel = Cpt(Signal, value=0, kind="omitted")
    low_limit_travel = Cpt(Signal, value=0, kind="omitted")

    SUB_READBACK = "readback"
    SUB_CONNECTION_CHANGE = "connection_change"
    _default_sub = SUB_READBACK

    def __init__(
        self,
        axis_Id,
        prefix="",
        *,
        name,
        kind=None,
        read_attrs=None,
        configuration_attrs=None,
        parent=None,
        host="mpc2680.psi.ch",
        port=8081,
        limits=None,
        sign=1,
        socket_cls=SocketIO,
        device_manager=None,
        **kwargs,
    ):
        self.controller = FlomniGalilController(
            socket_cls=socket_cls, socket_host=host, socket_port=port
        )
        self.axis_Id = axis_Id
        self.controller.set_axis(axis=self, axis_nr=self.axis_Id_numeric)
        self.sign = sign
        self.tolerance = kwargs.pop("tolerance", 0.5)
        self.device_mapping = kwargs.pop("device_mapping", {})
        self.device_manager = device_manager

        if len(self.device_mapping) > 0 and self.device_manager is None:
            raise BECConfigError(
                "device_mapping has been specified but the device_manager cannot be accessed."
            )
        self.rt = self.device_mapping.get("rt")
        self.pid_x_correction = 0

        super().__init__(
            prefix,
            name=name,
            kind=kind,
            read_attrs=read_attrs,
            configuration_attrs=configuration_attrs,
            parent=parent,
            **kwargs,
        )
        self.readback.name = self.name
        self.controller.subscribe(
            self._update_connection_state, event_type=self.SUB_CONNECTION_CHANGE
        )
        self._update_connection_state()
        # self.readback.subscribe(self._forward_readback, event_type=self.readback.SUB_VALUE)

        if limits is not None:
            assert len(limits) == 2
            self.low_limit_travel.put(limits[0])
            self.high_limit_travel.put(limits[1])

    @property
    def limits(self):
        return (self.low_limit_travel.get(), self.high_limit_travel.get())

    @property
    def low_limit(self):
        return self.limits[0]

    @property
    def high_limit(self):
        return self.limits[1]

    def check_value(self, pos):
        """Check that the position is within the soft limits"""
        low_limit, high_limit = self.limits

        if low_limit < high_limit and not (low_limit <= pos <= high_limit):
            raise LimitError(f"position={pos} not within limits {self.limits}")

    def _update_connection_state(self, **kwargs):
        for walk in self.walk_signals():
            walk.item._metadata["connected"] = self.controller.connected

    def _forward_readback(self, **kwargs):
        kwargs.pop("sub_type")
        self._run_subs(sub_type="readback", **kwargs)

    @raise_if_disconnected
    def move(self, position, wait=True, **kwargs):
        """Move to a specified position, optionally waiting for motion to
        complete.

        Parameters
        ----------
        position
            Position to move to
        moved_cb : callable
            Call this callback when movement has finished. This callback must
            accept one keyword argument: 'obj' which will be set to this
            positioner instance.
        timeout : float, optional
            Maximum time to wait for the motion. If None, the default timeout
            for this positioner is used.

        Returns
        -------
        status : MoveStatus

        Raises
        ------
        TimeoutError
            When motion takes longer than `timeout`
        ValueError
            On invalid positions
        RuntimeError
            If motion fails other than timing out
        """
        self._started_moving = False
        timeout = kwargs.pop("timeout", 100)
        status = super().move(position, timeout=timeout, **kwargs)
        self.user_setpoint.put(position, wait=False)

        def move_and_finish():
            while self.motor_is_moving.get():
                logger.info("motor is moving")
                val = self.readback.read()
                self._run_subs(sub_type=self.SUB_READBACK, value=val, timestamp=time.time())
                time.sleep(0.1)
            val = self.readback.read()
            success = np.isclose(val[self.name]["value"], position, atol=self.tolerance)

            if not success:
                print(" stop")
            self._done_moving(success=success)
            logger.info("Move finished")

        threading.Thread(target=move_and_finish, daemon=True).start()
        try:
            if wait:
                status_wait(status)
        except KeyboardInterrupt:
            self.stop()
            raise

        return status

    @property
    def axis_Id(self):
        return self._axis_Id_alpha

    @axis_Id.setter
    def axis_Id(self, val):
        if isinstance(val, str):
            if len(val) != 1:
                raise ValueError("Only single-character axis_Ids are supported.")
            self._axis_Id_alpha = val
            self._axis_Id_numeric = ord(val.lower()) - 97
        else:
            raise TypeError(f"Expected value of type str but received {type(val)}")

    @property
    def axis_Id_numeric(self):
        return self._axis_Id_numeric

    @axis_Id_numeric.setter
    def axis_Id_numeric(self, val):
        if isinstance(val, int):
            if val > 26:
                raise ValueError("Numeric value exceeds supported range.")
            self._axis_Id_alpha = val
            self._axis_Id_numeric = (chr(val + 97)).capitalize()
        else:
            raise TypeError(f"Expected value of type int but received {type(val)}")

    @property
    def egu(self):
        """The engineering units (EGU) for positions"""
        return "mm"

    def stage(self) -> list[object]:
        return super().stage()

    def unstage(self) -> list[object]:
        return super().unstage()

    def stop(self, *, success=False):
        self.controller.stop_all_axes()
        return super().stop(success=success)


# if __name__ == "__main__":
#     mock = False
#     if not mock:
#         leyey = GalilMotor("H", name="leyey", host="mpc2680.psi.ch", port=8081, sign=-1)
#         leyey.stage()
#         status = leyey.move(0, wait=True)
#         status = leyey.move(10, wait=True)
#         leyey.read()

#         leyey.get()
#         leyey.describe()

#         leyey.unstage()
#     else:
#         from ophyd_devices.utils.socket import SocketMock

#         leyex = GalilMotor(
#             "G", name="leyex", host="mpc2680.psi.ch", port=8081, socket_cls=SocketMock
#         )
#         leyey = GalilMotor(
#             "H", name="leyey", host="mpc2680.psi.ch", port=8081, socket_cls=SocketMock
#         )
#         leyex.stage()
#         # leyey.stage()

#         leyex.controller.galil_show_all()
