import os
import logging
from usb_device_control.logger import setup_logger

logger = setup_logger()

def unblock_usb(device):
    try:
        os.system(f"sudo udisksctl mount -b {device}")
        logger.info(f"Unblocked USB device: {device}")
    except Exception as e:
        logger.error(f"Failed to unblock USB device {device}: {str(e)}")
