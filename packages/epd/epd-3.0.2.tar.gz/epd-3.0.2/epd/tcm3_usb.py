'''
To use the TCM3 as USB device on a linux system, add the following rules to /etc/udev/rules.d/tcm.rules

SUBSYSTEMS=="usb", ATTRS{idVendor}=="6666", ATTRS{idProduct}=="6666", \
    MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1", \
    SYMLINK+="TCM_%n"

ACTION=="add", SUBSYSTEM=="usb_device", SYSFS{idVendor}=="6666", SYSFS{idProduct}=="6666", MODE="0666"
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="6666", ATTR{idProduct}=="6666", MODE="0666"
'''

import usb.core
import usb.util
from typing import Optional

class USBDevice:

    def __init__(self, vendor_id: int, product_id: int):
        self.vendor_id: int = vendor_id
        self.product_id: int = product_id
        self._device: Optional[usb.core.Device] = None
        self._get_device()

    def _get_device(self):
        device: Optional[usb.core.Device] = usb.core.find(find_all=False, idVendor=self.vendor_id, idProduct=self.product_id)
        if device is None:
            raise ValueError(f'Device ({self.vendor_id}:{self.product_id}) not found')
        device.set_configuration(1)
        self._device = device

    def read(self, endpoint: int, size_or_buffer, timeout: Optional[int] = None) -> bytes:
        try:
            return self._device.read(endpoint, size_or_buffer, timeout)
        except usb.core.USBError:
            self._get_device()
            return self._device.read(endpoint, size_or_buffer, timeout)

    def write(self, endpoint: int, data: bytes, timeout: Optional[int] = None):
        try:
            self._device.write(endpoint, data, timeout)
        except usb.core.USBError:
            self._get_device()
            self._device.write(endpoint, data, timeout)

    def __str__(self):
        return f'<USBDevice vendor_id={self.vendor_id}> product_id={self.product_id}> address={self._device.address}>'

if __name__=="__main__":
    dev = USBDevice(vendor_id=0x6666, product_id=0x6666)
