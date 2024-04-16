# -*- coding: UTF-8 -*-
"""
Abstract TCM class for version 3.

..  Copyright (C) MpicoSys-Embedded Pico Systems, all Rights Reserved.
    This source code and any compilation or derivative thereof is the
    proprietary information of MpicoSys and is confidential in nature.
    Under no circumstances is this software to be exposed to or placed
    under an Open Source License of any type without the expressed
    written permission of MpicoSys.
"""

__copyright__ = "Copyright (C) MpicoSys-Embedded Pico Systems"
__author__ = "Paweł Musiał <pawel.musial@mpicosys.com>"
__version__ = "1.0"

import epd.convert
import hashlib
import struct
import zlib # replace with crc32

class TCMWrongImage(Exception):
    def __init__(self, message):
        """ Class constructor. """
        self.msg = message

    def __str__(self):
        """ String representation of error. """
        return "Problem with provided image to TCM converter: %s" % self.msg

class TCGen3(object):
    # SYSTEM
    TCM_ENABLE = 0x01
    TCM_DISABLE = 0x02
    LED_CONTROL = 0x03

    # DISPLAY
    DISPLAY_UPDATE = 0x10
    WRITE_TO_DISPLAY = 0x11
    CLEAR_SCREEN = 0x12
    COPY_DISPLAY_TO_MEMORY = 0x13
    READ_FROM_DISPLAY = 0x14

    # MEMORY
    CHECK_FILE = 0x30
    WRITE_TO_MEMORY = 0x31
    CLEAR_MEMORY = 0x32
    COPY_MEMORY_TO_DISPLAY = 0x33
    READ_FROM_MEMORY = 0x34

    # GRAPHIC LIB
    PUT_STRING = 0x50
    PUT_STRING_WRAP = 0x51
    GET_STRING_WIDTH = 0x52
    CHANGE_ORIENTATION = 0x53
    DRAW_LINE = 0x54
    DRAW_CIRCLE = 0x55
    DRAW_RECTANGLE = 0x56

    # SYSTEM CONTROL
    GET_SYSTEM_INFO = 0x70
    GET_UNIQUE_ID = 0x71
    LEDS_CONTROL = 0x72
    GET_LEDS_DATA = 0x73
    GET_LIGHTING_DATA = 0x74
    GET_TEMPERATURE = 0x75
    GET_VCOM = 0x76
    SET_VCOM = 0x77

    # DEVELOPMENT CONFIG
    UPLOAD_NEW_FIRMWARE = 0x90
    JUMP_TO_APP = 0x91
    JUMP_TO_BOOT = 0x92
    ERASE_ENTIRE_RAM = 0x93
    ERASE_ENTIRE_FLASH = 0x94
    SYSTEM_RESTART = 0x95
    GET_DISPLAY_INFO = 0x96
    GET_CONFIG_DATA = 0x97

    def __init__(self):
        self.compression = False

    def get_epd_file(self,img,filename=None):
        if len(img.getcolors()) > 2: # TODO check if imge is paletted
            raise TCMWrongImage("Image has more colors than 2")
        bits = 1 # change to support more bits
        data = epd.convert.toType0_1bit(img.tobytes())
        if filename is None:
            # use image hash as file name
            filename = hashlib.sha1(data).hexdigest()[:16]
        return b'EPD' + struct.pack("<BHHII16s", 48 + bits, img.width, img.height, len(data), zlib.crc32(data), bytes(filename.encode('ascii')) ) + data
        # return b'EPD' + struct.pack("<BHHII16s", 48 + bits, img.width, img.height, len(data), epd.convert.crc32(data), filename) + data

    def parse_response(self, response):

        error_code = [
                "NORMAL_PROCESSING", "INSTRUCTION_NOT_SUPPORTED", "WRONG_PARAMETERS", "WRONG_HEADER", "WRONG_CRC",
                "WRONG_LENGTH", "MEMORY_FAILURE", "DCDC_ERROR", "I2C_ERROR"
            ]

        command = [
                "TCM_ENABLE", "TCM_DISABLE", "LED_CONTROL", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                "DISPLAY_UPDATE", "WRITE_TO_DISPLAY", "CLEAR_SCREEN", "COPY_DISPLAY_TO_MEMORY", "READ_FROM_DISPLAY",
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                "CHECK_FILE", "WRITE_TO_MEMORY", "CLEAR_MEMORY", "COPY_MEMORY_TO_DISPLAY", "READ_FROM_MEMORY",
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                "PUT_STRING", "PUT_STRING_WRAP", "GET_STRING_WIDTH", "CHANGE_ORIENTATION", "DRAW_LINE",
                "DRAW_CIRCLE", "DRAW_RECTANGLE", 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                "GET_SYSTEM_INFO", "GET_UNIQUE_ID", "LEDS_CONTROL", "GET_LEDS_DATA",
                "GET_LIGHTING_DATA", "GET_TEMPERATURE", "GET_VCOM", "SET_VCOM", 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                "UPLOAD_NEW_FIRMWARE", "SWITCH_TO_APP", "SWITCH_TO_BOOT", "ERASE_ENTIRE_RAM", "ERASE_ENTIRE_FLASH", "SYSTEM_RESTART",
                "GET_DISPLAY_INFO", "GET_CONFIG_DATA",
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ]
        print("command: " + hex(struct.unpack("B", response[0:1])[0]) + " --> " + command[struct.unpack("B", response[0:1])[0]])
        print("error_code: " + str(struct.unpack("B", response[1:2])[0]) + " --> " + error_code[struct.unpack("B", response[1:2])[0]])


    def DisplayUpdate(self, waveform=0): # TODO: add waveform validation
        return struct.pack('<BB', self.DISPLAY_UPDATE, waveform)

    def WriteToDisplay(self, datafile, position_x=0, position_y=0): # TODO add address and position validation
        return struct.pack('<BHH', self.WRITE_TO_DISPLAY, position_x, position_y) + datafile

    def ClearScreen(self, color=0x0):
        return struct.pack('<BB', self.CLEAR_SCREEN, color)

    def CopyDisplayToMemory(self, address): # TODO add address validation
        return struct.pack('<BI', self.COPY_DISPLAY_TO_MEMORY, address)

    def ReadFromDisplay(self): # TODO is this removed?
        return struct.pack('<BBBB', self.READ_FROM_DISPLAY, 0, 0, 0)

    def CheckFile(self, address):
        return struct.pack('<BI', self.CHECK_FILE, address)

    def WriteToMemory(self, address, datafile):
        return struct.pack('<BI', self.WRITE_TO_MEMORY, address) + datafile

    def CopyMemoryToDisplay(self, address, position_x, position_y, colormode=0):
        return struct.pack('<BBIHH', self.COPY_MEMORY_TO_DISPLAY, colormode, address, position_x, position_y)

    def ReadFromMemory(self, address): # TODO is this removed?
        return struct.pack('<BBBBI', self.READ_FROM_MEMORY, 0, 0, 0, address)

    def PutString(self, fontid, color, position_x, position_y, string):
        return struct.pack('<BBBHH', self.PUT_STRING, fontid, color, position_x, position_y) + string.encode('ascii')

    def PutStringWrap(self, fontid, color, position_x, position_y, position_x2, position_y2, string):
        return struct.pack('<BBBHHHH', self.PUT_STRING_WRAP, fontid, color, position_x, position_y, position_x2, position_y2) + string.encode('ascii')




class GetUniqueId:
    CMD_CODE = 0x71
    def prepare(self,*args, **kwargs):
        return struct.pack('<BBBB', self.CMD_CODE, 0, 0, 0)

    def handle_response(self, data):
        response = {'command': data[0], "error_code": data[1]}
        if len(data) > 2:
            response['response'] = {
                'unique_id': list(data[2:])
            }
        return response

class GetSystemInfo:
    CMD_CODE = 0x70
    def prepare(self,*args, **kwargs):
        return struct.pack('<BBBB', self.CMD_CODE, 0, 0, 0)

    def handle_response(self, data):
        response = {'command': data[0],"error_code":data[1]}
        if len(data) > 2:
            disp_info = struct.unpack("<BBBBHHBBHIII", data[2:])
            response['response'] = {
                'version': f"{disp_info[0]}.{disp_info[1]}",
                'panel_size': f"{disp_info[2]}.{disp_info[3]}",
                'width':disp_info[4],
                'height': disp_info[5],
                'fonts_number':disp_info[6],
                'hw_version': disp_info[7],
                'sector_size': disp_info[8],
                'sector_number': disp_info[9],
                'app_size': disp_info[10],
                'app_crc': disp_info[11]
            }
        return response

