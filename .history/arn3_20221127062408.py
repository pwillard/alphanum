#!/usr/bin/python
"""Script to generate small bitmaps with white numbers on
an alpha background. The output is a set of TGA files for use
with various train simulation numbering features.

Basic usage:
$ python3 arn.py  (No file options are needed)

You need to edit values in the top of this file to change defaults
This code has been tested with Python 3.10.4 and requires the use of
the Python package "PILLOW".

To install PILLOW, use:

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

=============================

Author: Pete Willard
Email: petewillard@gmail.com
Website: RailSimStuff.com
Date: April 5, 2022

Typically 64x64 bitmap is ok and use just the numbers. 
Well, numbers make sense but you never know, there 
is this guy at RailSimStuff.com that puts numbers 
on !@#$%^&*() characters.

"""

from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import configparser

# Set Image Size and the font's characters we will use
settings = 'config.ini'
path = Path(settings)

# If we don't have an INI file, use defaults

if path.is_file():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    parser.sections()
    numberlist = parser.get('settings','numberList')
    height = int(parser.get('settings','height'))
    width = int(parser.get('settings','width'))
    fontSize = int(parser.get('settings','fontSize'))
    fontHorz = int(parser.get('settings','fontHorz'))
    fontVert = int(parser.get('settings','fontVert'))
    pathToFont = parser.get('settings','pathToFont')
    fontColor = int(parser.get('settings','fontColor'))
else:
    numberList = "0123456789"
    height = 64
    width = 64
    # You will need to tweak these values below based on the 
    # specific font being used so it fits the 'box' correctly
    fontSize = 68 
    fontHorz = 10
    fontVert = -4
    pathToFont = "c:/temp/consolidated.ttf"
    fontColor = "255"


if __name__ == '__main__':
 
    # get the font
    # 
    fnt = ImageFont.truetype(pathToFont, fontSize)


    """
     Draw Character Black on White Background
     then invert to White on Black Background (it's just easier)
     since we can rely on defaults

     We are looping through each member of the numberList
     and writing out each character result individually    
    """
    count = 0

    for element in numberList:
        #Setup
        image = Image.new(mode='L', size=(height, width), color=0)
        draw = ImageDraw.Draw(image)
        #
        draw.text((fontHorz,fontVert),element,font=fnt,fill=255)
        

        
        # Save out the results
        out = "digit_" + str(count) + ".tga"
        count = count +1
        image.save(out,"TGA")






    