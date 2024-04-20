from unittest import mock

import pytest
from utils import SocketMock

from ophyd_devices.smaract import SmaractController
from ophyd_devices.smaract.smaract_controller import SmaractCommunicationMode
from ophyd_devices.smaract.smaract_errors import SmaractCommunicationError, SmaractErrorCode
from ophyd_devices.smaract.smaract_ophyd import SmaractMotor


@pytest.fixture
def controller():
    SmaractController._reset_controller()
    controller = SmaractController(socket_cls=SocketMock, socket_host="dummy", socket_port=123)
    controller.on()
    controller.sock.flush_buffer()
    yield controller


@pytest.fixture
def lsmarA():
    SmaractController._reset_controller()
    motor_a = SmaractMotor(
        "A", name="lsmarA", host="mpc2680.psi.ch", port=8085, sign=1, socket_cls=SocketMock
    )
    motor_a.controller.on()
    motor_a.controller.sock.flush_buffer()
    motor_a.stage()
    yield motor_a


@pytest.mark.parametrize(
    "axis,position,get_message,return_msg",
    [
        (0, 50, b":GP0\n", b":P0,50000000\n"),
        (1, 0, b":GP1\n", b":P1,0\n"),
        (0, -50, b":GP0\n", b":P0,-50000000\n"),
        (0, -50.23, b":GP0\n", b":P0,-50230000\n"),
    ],
)
def test_get_position(controller, axis, position, get_message, return_msg):
    controller.sock.buffer_recv = return_msg
    val = controller.get_position(axis)
    assert val == position
    assert controller.sock.buffer_put[0] == get_message


@pytest.mark.parametrize(
    "axis,is_referenced,get_message,return_msg,exception",
    [
        (0, True, b":GPPK0\n", b":PPK0,1\n", None),
        (1, True, b":GPPK1\n", b":PPK1,1\n", None),
        (0, False, b":GPPK0\n", b":PPK0,0\n", None),
        (200, False, b":GPPK0\n", b":PPK0,0\n", ValueError),
    ],
)
def test_axis_is_referenced(controller, axis, is_referenced, get_message, return_msg, exception):
    controller.sock.buffer_recv = return_msg
    if exception is not None:
        with pytest.raises(exception):
            val = controller.axis_is_referenced(axis)
    else:
        val = controller.axis_is_referenced(axis)
        assert val == is_referenced
        assert controller.sock.buffer_put[0] == get_message


@pytest.mark.parametrize(
    "return_msg,exception,raised",
    [
        (b"false\n", SmaractCommunicationError, False),
        (b":E0,1", SmaractErrorCode, True),
        (b":E,1", SmaractCommunicationError, True),
        (b":E,-1", SmaractCommunicationError, True),
    ],
)
def test_socket_put_and_receive_raises_exception(controller, return_msg, exception, raised):
    controller.sock.buffer_recv = return_msg
    with pytest.raises(exception):
        controller.socket_put_and_receive(b"test", raise_if_not_status=True)

    controller.sock.flush_buffer()
    controller.sock.buffer_recv = return_msg

    if raised:
        with pytest.raises(exception):
            controller.socket_put_and_receive(b"test")
    else:
        assert controller.socket_put_and_receive(b"test") == return_msg.split(b"\n")[0].decode()


@pytest.mark.parametrize(
    "mode,get_message,return_msg", [(0, b":GCM\n", b":CM0\n"), (1, b":GCM\n", b":CM1\n")]
)
def test_communication_mode(controller, mode, get_message, return_msg):
    controller.sock.buffer_recv = return_msg
    val = controller.get_communication_mode()
    assert controller.sock.buffer_put[0] == get_message
    assert val == SmaractCommunicationMode(mode)


@pytest.mark.parametrize(
    "is_moving,get_message,return_msg",
    [
        (0, b":GS0\n", b":S0,0\n"),
        (1, b":GS0\n", b":S0,1\n"),
        (1, b":GS0\n", b":S0,2\n"),
        (0, b":GS0\n", b":S0,3\n"),
        (1, b":GS0\n", b":S0,4\n"),
        (0, b":GS0\n", b":S0,5\n"),
        (0, b":GS0\n", b":S0,6\n"),
        (1, b":GS0\n", b":S0,7\n"),
        (0, b":GS0\n", b":S0,9\n"),
        (0, [b":GS0\n", b":GS0\n"], [b":E0,0\n", b":S0,9"]),
    ],
)
def test_axis_is_moving(controller, is_moving, get_message, return_msg):
    controller.sock.buffer_recv = return_msg
    val = controller.is_axis_moving(0)
    assert val == is_moving
    if isinstance(controller.sock.buffer_put, list) and len(controller.sock.buffer_put) == 1:
        controller.sock.buffer_put = controller.sock.buffer_put[0]
    assert controller.sock.buffer_put == get_message


@pytest.mark.parametrize(
    "sensor_id,axis,get_msg,return_msg",
    [
        (1, 0, b":GST0\n", b":ST0,1\n"),
        (6, 0, b":GST0\n", b":ST0,6\n"),
        (6, 1, b":GST1\n", b":ST1,6\n"),
    ],
)
def test_get_sensor_definition(controller, sensor_id, axis, get_msg, return_msg):
    controller.sock.buffer_recv = return_msg
    sensor = controller.get_sensor_type(axis)
    assert sensor.type_code == sensor_id


@pytest.mark.parametrize(
    "move_speed,axis,get_msg,return_msg",
    [
        (50, 0, b":SCLS0,50000000\n", b":E-1,0"),
        (0, 0, b":SCLS0,0\n", b":E-1,0"),
        (20.23, 1, b":SCLS1,20230000\n", b":E-1,0"),
    ],
)
def test_set_move_speed(controller, move_speed, axis, get_msg, return_msg):
    controller.sock.buffer_recv = return_msg
    controller.set_closed_loop_move_speed(axis, move_speed)
    assert controller.sock.buffer_put[0] == get_msg


@pytest.mark.parametrize(
    "pos,axis,hold_time,get_msg,return_msg",
    [
        (50, 0, None, b":MPA0,50000000,1000\n", b":E0,0"),
        (0, 0, 800, b":MPA0,0,800\n", b":E0,0"),
        (20.23, 1, None, b":MPA1,20230000,1000\n", b":E0,0"),
    ],
)
def test_move_axis_to_absolute_position(controller, pos, axis, hold_time, get_msg, return_msg):
    controller.sock.buffer_recv = return_msg
    if hold_time is not None:
        controller.move_axis_to_absolute_position(axis, pos, hold_time=hold_time)
    else:
        controller.move_axis_to_absolute_position(axis, pos)
    assert controller.sock.buffer_put[0] == get_msg


@pytest.mark.parametrize(
    "pos,get_msg,return_msg",
    [
        (
            50,
            [b":GPPK0\n", b":MPA0,50000000,1000\n", b":GS0\n", b":GP0\n"],
            [b":PPK0,1\n", b":E0,0\n", b":S0,0\n", b":P0,50000000\n"],
        ),
        (
            0,
            [b":GPPK0\n", b":MPA0,0,1000\n", b":GS0\n", b":GP0\n"],
            [b":PPK0,1\n", b":E0,0\n", b":S0,0\n", b":P0,0000000\n"],
        ),
        (
            20.23,
            [b":GPPK0\n", b":MPA0,20230000,1000\n", b":GS0\n", b":GP0\n"],
            [b":PPK0,1\n", b":E0,0\n", b":S0,0\n", b":P0,20230000\n"],
        ),
        (
            20.23,
            [b":GPPK0\n", b":GPPK0\n", b":MPA0,20230000,1000\n", b":GS0\n", b":GP0\n"],
            [b":S0,0\n", b":PPK0,1\n", b":E0,0\n", b":S0,0\n", b":P0,20230000\n"],
        ),
    ],
)
def test_move_axis(lsmarA, pos, get_msg, return_msg):
    controller = lsmarA.controller
    controller.sock.buffer_recv = return_msg
    lsmarA.move(pos)
    assert controller.sock.buffer_put == get_msg


@pytest.mark.parametrize("num_axes,get_msg,return_msg", [(1, [b":S0\n"], [b":E0,0"])])
def test_stop_axis(lsmarA, num_axes, get_msg, return_msg):
    controller = lsmarA.controller
    controller.sock.buffer_recv = return_msg
    controller.stop_all_axes()
    assert controller.sock.buffer_put == get_msg


def test_all_axes_referenced(lsmarA):
    controller = lsmarA.controller
    with mock.patch.object(controller, "axis_is_referenced", return_value=True) as mock_is_ref:
        val = controller.all_axes_referenced()
        assert val
        mock_is_ref.assert_called_once_with(0)
