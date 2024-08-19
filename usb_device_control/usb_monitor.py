import psutil
import logging
from usb_device_control.logger import setup_logger

logger = setup_logger()

class USBMonitor:
    def __init__(self):
        self.previous_devices = set(self.list_usb_devices())

    def list_usb_devices(self):
        devices = set()
        for device in psutil.disk_partitions():
            if 'usb' in device.opts:
                devices.add(device.device)
        return devices

    def check_changes(self):
        current_devices = set(self.list_usb_devices())
        added = current_devices - self.previous_devices
        removed = self.previous_devices - current_devices
        self.previous_devices = current_devices
        if added:
            logger.info(f"USB devices added: {added}")
        if removed:
            logger.info(f"USB devices removed: {removed}")
        return added, removed
