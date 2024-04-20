import functools
import threading
import time

import numpy as np
from bec_lib import bec_logger
from ophyd import Component as Cpt
from ophyd import Device, PositionerBase, Signal
from ophyd.status import wait as status_wait
from ophyd.utils import LimitError, ReadOnlyError
from prettytable import PrettyTable

from ophyd_devices.galil.galil_ophyd import (
    BECConfigError,
    GalilAxesReferenced,
    GalilCommunicationError,
    GalilController,
    GalilError,
    GalilMotorIsMoving,
    GalilMotorResolution,
    GalilReadbackSignal,
    GalilSetpointSignal,
    retry_once,
)
from ophyd_devices.utils.controller import Controller, threadlocked
from ophyd_devices.utils.socket import SocketIO, SocketSignal, raise_if_disconnected

logger = bec_logger.logger


class FuprGalilController(GalilController):
    _axes_per_controller = 1

    def is_axis_moving(self, axis_Id, axis_Id_numeric) -> bool:
        if axis_Id is None and axis_Id_numeric is not None:
            axis_Id = self.axis_Id_numeric_to_alpha(axis_Id_numeric)
        is_moving = bool(float(self.socket_put_and_receive(f"MG_BG{axis_Id}")) != 0)
        return is_moving

    def axis_is_referenced(self, axis_Id) -> bool:
        return self.all_axes_referenced()

    def all_axes_referenced(self) -> bool:
        return bool(float(self.socket_put_and_receive("MG axisref").strip()))

    def drive_axis_to_limit(self, axis_Id_numeric, direction: str) -> None:
        raise NotImplementedError("This function is not implemented for the FuprGalilController.")


class FuprGalilReadbackSignal(GalilReadbackSignal):
    @retry_once
    @threadlocked
    def _socket_get(self) -> float:
        """Get command for the readback signal

        Returns:
            float: Readback value after adjusting for sign and motor resolution.
        """

        current_pos = float(self.controller.socket_put_and_receive(f"TP{self.parent.axis_Id}"))
        current_pos *= self.parent.sign
        step_mm = self.parent.motor_resolution.get()
        return current_pos / step_mm

    def read(self):
        self._metadata["timestamp"] = time.time()
        val = super().read()
        if self.parent.axis_Id_numeric == 0:
            try:
                rt = self.parent.device_manager.devices[self.parent.rt]
                if rt.enabled:
                    rt.obj.controller.set_rotation_angle(val[self.parent.name]["value"])
            except KeyError:
                logger.warning("Failed to set RT value during readback.")
        return val


class FuprGalilSetpointSignal(GalilSetpointSignal):
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
            self.controller.socket_put_confirmed(
                f"PA{self.parent.axis_Id}={int(self.setpoint*self.parent.MOTOR_RESOLUTION)}"
            )
            self.controller.socket_put_confirmed(f"BG{self.parent.axis_Id}")
        else:
            raise GalilError("Not all axes are referenced.")


class FuprGalilMotorResolution(GalilMotorResolution):
    @retry_once
    @threadlocked
    def _socket_get(self):
        return self.parent.MOTOR_RESOLUTION


class FuprGalilMotorIsMoving(GalilMotorIsMoving):
    pass


class FuprGalilAxesReferenced(GalilAxesReferenced):
    pass


class FuprGalilMotor(Device, PositionerBase):
    USER_ACCESS = ["controller"]
    MOTOR_RESOLUTION = 25600
    readback = Cpt(FuprGalilReadbackSignal, signal_name="readback", kind="hinted")
    user_setpoint = Cpt(FuprGalilSetpointSignal, signal_name="setpoint")
    motor_resolution = Cpt(FuprGalilMotorResolution, signal_name="resolution", kind="config")
    motor_is_moving = Cpt(FuprGalilMotorIsMoving, signal_name="motor_is_moving", kind="normal")
    all_axes_referenced = Cpt(
        FuprGalilAxesReferenced, signal_name="all_axes_referenced", kind="config"
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
        self.controller = FuprGalilController(
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
        self.rt = self.device_mapping.get("rt", "rtx")

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
                raise ValueError(f"Only single-character axis_Ids are supported.")
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
                raise ValueError(f"Numeric value exceeds supported range.")
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
