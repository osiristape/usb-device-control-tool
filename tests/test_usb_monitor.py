import unittest
from usb_device_control.usb_monitor import USBMonitor

class TestUSBMonitor(unittest.TestCase):
    def test_list_usb_devices(self):
        monitor = USBMonitor()
        devices = monitor.list_usb_devices()
        self.assertIsInstance(devices, set)

    def test_check_changes(self):
        monitor = USBMonitor()
        added, removed = monitor.check_changes()
        self.assertIsInstance(added, set)
        self.assertIsInstance(removed, set)
