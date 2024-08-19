import os
import logging
from usb_device_control.logger import setup_logger

logger = setup_logger()

def block_usb(device):
    try:
        os.system(f"sudo udisksctl unmount -b {device}")
        logger.info(f"Blocked USB device: {device}")
    except Exception as e:
        logger.error(f"Failed to block USB device {device}: {str(e)}")
