import unittest
from usb_device_control.utils import setup_logger

class TestUtils(unittest.TestCase):
    def test_setup_logger(self):
        logger = setup_logger('test_logger')
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, 'test_logger')
