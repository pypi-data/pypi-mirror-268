# -*- coding: utf-8 -*-
# from distutils.core import setup, Extension
from setuptools import setup, Extension

#import distutils.log
#distutils.log.set_verbosity(distutils.log.DEBUG) # Set DEBUG level

c_convert = Extension('c_convert',
                    sources = ['epdconvert/src/lz.c',
                               'epdconvert/src/epdconvert.c',
                               'epdconvert/src/Compression.c',
                               'epdconvert/src/Type0.c',
                               'epdconvert/src/Type2.c',
                               'epdconvert/src/Type7.c',
                               'epdconvert/src/Invert.c',
                               'epdconvert/src/Flip.c',
                               'epdconvert/src/Chunks.c',
                               'epdconvert/src/crc32.c'],
                    include_dirs=['epdconvert/include/',],
                    language='c',
                    extra_compile_args = ["-std=c99"],
                  )

c_kaleido = Extension('epd.kaleido',
                    sources = [
                        'c_kaleido/src/c_kaleido.c',
                        'c_kaleido/src/1bpp.c',
                        'c_kaleido/src/2bpp.c',
                        'c_kaleido/src/4bpp.c',
                    ],
                    include_dirs=['c_kaleido/include/',],
                    language='c',
                    extra_compile_args = ["-std=c99"],
                  )

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup (name = 'epd',
       version = '3.0.2',
       author="Paweł Musiał, MpicoSys",
       url="https://www.mpicosys.com/",
       author_email='pawel.musial@mpicosys.com',
       description = 'EPD library for MpicoSys Timing Controllers (TC/TCM), including color conversion',
       ext_modules = [c_convert,c_kaleido],
       packages = ['epd','epd.tcm','epd.convert',],
       requires = ['Pillow','hashlib'],
       long_description=long_description,
       long_description_content_type='text/markdown'
       )