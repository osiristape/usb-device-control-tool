import unittest
from unittest.mock import patch
from usb_device_control.usb_unblock import unblock_usb

class TestUSBUnblock(unittest.TestCase):
    @patch('usb_device_control.usb_unblock.os.system')
    def test_unblock_usb(self, mock_system):
        unblock_usb('/dev/sdb')
        mock_system.assert_called_with('sudo udisksctl mount -b /dev/sdb')
