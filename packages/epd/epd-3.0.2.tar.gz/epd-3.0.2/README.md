# EPD (ePaper Display) library for MpicoSys Timing Controller Modules (TCM) for E Ink displays

MpicoSys timing controllers (TCM) can be used to drive large size E ink displays, providing the conversion from an image 
file to the timing signals that are needed to display the image on the screen.
The MpicoSys TCMs use a specific image file format (.epd) to send the image data to the TCM. 
This Library provides tools to convert any image format to the MpicoSys .epd format.

## Available MpicoSys TCM's for E ink displays 
There are currently two generations of TCM's available TCM2 (generation2) and TCM3 (Generation3), 
where TCM3 offers a graphical library. 
TCM2 and TCM3 are available in 2 versions - Flash for limited number of updates and SRAM for high amount of updates, 
e.g. Realtime Passenger Information.

1) TCM for Monochrome (B/W) E Ink displays

| Display  | E-INK code   | MpicoSys TCM  |
|----------|--------------|---------------|
| 7.8"     | ED078KC1     | TCM2          |
| 9.7"     | ED097TC2     | TCM2          |
| 11.3"    | ED113TC1     | TCM2          |
| 13.3"    | ED133UT2/UT3 | TCM2 and TCM3 |
| 28"      |              | TCM3          | 
| 31.2"    | ED312TT2     | TCM2          |
| 42"      | ED420TT1     | TCM2          |

2) TCM3 for COLOR - Kaleido E Ink displays - SRAM version 

| Display | E-INK code   | MpicoSys TCM |
|---------|--------------|--------------|
| 13.3"   | 	SD1452-NCB| 	TCM3        |


The differences between TCM2 and TCM3 are

|     | TCM2  |TCM3|
|-----|----|----|
|Interface|SPI|RS485 or USB|
|Greylevels|2 or 4|2,4 or 16|
|Graphical lib|no|yes|	 

### How to find out controller version?
The TCM3 boards have a printed logo "Timing controller Module V3" 


## TCM3 (Timing Controller Module version 3)
The example below uses USB to connect to the TCM3 from the host.

This library requires:
- Pillow (image conversion)
- pyusb (for use with TCM as USB device, test code)

### Black-white, grey scale

```python
import epd.tcm3_usb
import epd.tcm.TCGen3
import epd.image
from PIL import Image
import os

path = os.path.dirname(os.path.abspath(__file__))

dev = epd.tcm3_usb.USBDevice(vendor_id=0x6666, product_id=0x6666)
TCM3 = epd.tcm.TCGen3.TCGen3()

# for BW display
img = Image.open(os.path.join(path,"skm.png"))              # open image
img = epd.image.pilimage_to_1bit(img)                       # make sure the image is: paletted and 1 bit only
                                                            # conversion to 2 bit and 4 bit to be done

epd_file = TCM3.get_epd_file(img=img)                       # create epd file data format
epd_file_command = TCM3.WriteToDisplay(epd_file)            # create epd command with file data

dev.write(0x01, epd_file_command)                           # send file to usb device (default endpoint 0x01)
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response

dev.write(0x01, TCM3.DisplayUpdate(0))                       # send Display Update command to the display
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response
```

see full example at: epd.test.epd_test_tcm3

### Color, E Ink Kaleido&trade; 
As for now (20-03-2024) this library was tested on 13.3 E Ink Kaleido display only.
https://shopkits.eink.com/en/product/detail/13.3%27%27Kaleido3ePaperDisplay
The color is achieved by having a color fiter on each pixel (CFA, color filter array)

```python
import epd.tcm3_usb
import epd.tcm.TCGen3
import epd.kaleido
from PIL import Image
import os

path = os.path.dirname(os.path.abspath(__file__))

dev = epd.tcm3_usb.USBDevice(vendor_id=0x6666, product_id=0x6666)
TCM3 = epd.tcm.TCGen3.TCGen3()

img = Image.open(os.path.join(path,"domek.jpg"))            # open image

# for kaleido colour display 1 bit per pixel driving
epd_file = epd.kaleido.convert_1bpp(img.tobytes())          # convert image bytes to epd TCM3 file format

epd_file_command = TCM3.WriteToDisplay(epd_file)            # create epd command with file data

dev.write(0x01, epd_file_command)                           # send file to usb device (default endpoint 0x01)
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response

dev.write(0x01, TCM3.DisplayUpdate())                       # send Display Update command to the display
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response


# for kaleido colour display 2 bit per pixel driving
epd_file = epd.kaleido.convert_2bpp(img.tobytes())          # convert image bytes to epd TCM3 file format

epd_file_command = TCM3.WriteToDisplay(epd_file)            # create epd command with file data

dev.write(0x01, epd_file_command)                           # send file to usb device (default endpoint 0x01)
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response

dev.write(0x01, TCM3.DisplayUpdate())                       # send Display Update command to the display
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response


# for kaleido colour display 4 bit per pixel driving
epd_file = epd.kaleido.convert_4bpp(img.tobytes())          # convert image bytes to epd TCM3 file format

epd_file_command = TCM3.WriteToDisplay(epd_file)            # create epd command with file data

dev.write(0x01, epd_file_command)                           # send file to usb device (default endpoint 0x01)
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response

dev.write(0x01, TCM3.DisplayUpdate())                       # send Display Update command to the display
TCM3.parse_response(dev.read(0x81, 60, 5000))               # read response
```




## TCM2 (Timing Controller Module version 2)
This library consist of the following parts:
- image preparation for use with 1 and 2 bit color ePaper display,
- image conversion and compression to TCM format,
- commands formatting for use with TCM,

### Image preparation
```python

from PIL import Image
import epd.image

img = Image.open("test_image.png")
img1bit = epd.image.pilimage_to_1bit(img)
img2bit = epd.image.pilimage_to_2bit(img)

### Image conversion to EPD data
import epd.convert
not_compressed_epd_data = epd.convert.toType0_1bit(img1bit.tobytes())
compressed_data =  epd.convert.compress_lz(no_compressed_data)

### TCM Commands formatting 
import epd.tcm

img = Image.open("test_133_image.png")
tcm = epd.tcm.TCM(system_version_code)
epd_data = tcm.get_epd_header(img)+tcm.convert(img)
```

&copy; MpicoSys 2024