import unittest
from unittest.mock import patch
from usb_device_control.usb_block import block_usb

class TestUSBBlock(unittest.TestCase):
    @patch('usb_device_control.usb_block.os.system')
    def test_block_usb(self, mock_system):
        block_usb('/dev/sdb')
        mock_system.assert_called_with('sudo udisksctl unmount -b /dev/sdb')
