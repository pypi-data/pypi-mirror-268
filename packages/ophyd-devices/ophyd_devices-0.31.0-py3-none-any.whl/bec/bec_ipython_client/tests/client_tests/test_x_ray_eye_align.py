from unittest import mock

from bec_ipython_client.plugins.LamNI import LamNI, XrayEyeAlign
from bec_lib.device import DeviceBase

# pylint: disable=unused-import


# pylint: disable=no-member
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=protected-access


class RTControllerMock:
    def feedback_disable(self):
        pass

    def feedback_enable_with_reset(self):
        pass


class RTMock(DeviceBase):
    controller = RTControllerMock()
    enabled = True


def test_save_frame(bec_client_mock):
    client = bec_client_mock
    client.device_manager.devices.xeye = DeviceBase(name="xeye", config={})
    lamni = LamNI(client)
    align = XrayEyeAlign(client, lamni)
    with mock.patch("bec_ipython_client.plugins.LamNI.x_ray_eye_align.epics_put") as epics_put_mock:
        align.save_frame()
        epics_put_mock.assert_called_once_with("XOMNYI-XEYE-SAVFRAME:0", 1)


def test_update_frame(bec_client_mock):
    epics_put = "bec_ipython_client.plugins.LamNI.x_ray_eye_align.epics_put"
    epics_get = "bec_ipython_client.plugins.LamNI.x_ray_eye_align.epics_get"
    fshopen = "bec_ipython_client.plugins.LamNI.x_ray_eye_align.fshopen"
    client = bec_client_mock
    client.device_manager.devices.xeye = DeviceBase(name="xeye", config={})
    lamni = LamNI(client)
    align = XrayEyeAlign(client, lamni)
    with mock.patch(epics_put) as epics_put_mock:
        with mock.patch(epics_get) as epics_get_mock:
            with mock.patch(fshopen) as fshopen_mock:
                align.update_frame()
                epics_put_mock.assert_has_calls(
                    [
                        mock.call("XOMNYI-XEYE-ACQDONE:0", 0),
                        mock.call("XOMNYI-XEYE-ACQ:0", 1),
                        mock.call("XOMNYI-XEYE-ACQDONE:0", 0),
                        mock.call("XOMNYI-XEYE-ACQ:0", 0),
                    ]
                )
                fshopen_mock.assert_called_once()
                epics_get_mock.assert_called_with("XOMNYI-XEYE-ACQDONE:0")


def test_disable_rt_feedback(bec_client_mock):
    client = bec_client_mock
    client.device_manager.devices.xeye = DeviceBase(name="xeye", config={})
    lamni = LamNI(client)
    align = XrayEyeAlign(client, lamni)
    client.device_manager.devices.rtx = RTMock(name="rtx", config={})
    with mock.patch.object(
        align.device_manager.devices.rtx.controller, "feedback_disable"
    ) as fdb_disable:
        align._disable_rt_feedback()
        fdb_disable.assert_called_once()


def test_enable_rt_feedback(bec_client_mock):
    client = bec_client_mock
    client.device_manager.devices.xeye = DeviceBase(name="xeye", config={})
    lamni = LamNI(client)
    align = XrayEyeAlign(client, lamni)
    client.device_manager.devices.rtx = RTMock(name="rtx", config={})
    with mock.patch.object(
        align.device_manager.devices.rtx.controller, "feedback_enable_with_reset"
    ) as fdb_enable:
        align._enable_rt_feedback()
        fdb_enable.assert_called_once()


def test_tomo_rotate(bec_client_mock):
    import builtins

    client = bec_client_mock
    client._ip = mock.MagicMock()
    client._update_namespace_callback = mock.MagicMock()
    client.callbacks = mock.MagicMock()
    client.load_high_level_interface("bec_hli")
    client.device_manager.devices.xeye = DeviceBase(name="xeye", config={})
    lamni = LamNI(client)
    align = XrayEyeAlign(client, lamni)
    client.device_manager.devices.lsamrot = RTMock(name="lsamrot", config={})
    with mock.patch.object(builtins, "umv") as umv:
        align.tomo_rotate(5)
        umv.assert_called_once_with(client.device_manager.devices.lsamrot, 5)
