#!/usr/bin/python
"""Script to generate small bitmaps with white numbers on
an alpha background. The output is a set of PNG files for use
with Trainz Autonumbering feature.

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


if __name__ == '__main__':
    # Set Image Size and the font's characters we will use

    numberList = "0123456789"
    height = 64
    width = 64
    # You will need to tweak these values below based on the 
    # specific font being used so it fits the 'box' correctly
    fontSize = 68 
    fontHorz = 10
    fontVert = -4
    pathToFont = "c:/temp/consolidated.ttf"
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
        image = Image.new(mode='L', size=(height, width), color=255)
        draw = ImageDraw.Draw(image)
        #
        draw.text((fontHorz,fontVert),element,font=fnt)
        # Invert to White Letters on Black Background
        img_invert =ImageOps.invert(image)
        # Convert image so we can play with RGB values
        rgba = img_invert.convert("RGBA")
        # Load raw image data so we can manipulate it
        imgData = rgba.getdata()
        # Replace RGB 'black' with Alpha.
        revisedRGB = []
        """ 
        The RGB value of black is (0, 0, 0). We will loop 
        through the data (RGBA values) and whenever we find a 
        black pixel we will replace it with a transparent 
        RGBA value which is ((255, 255, 255, 0), and the other 
        colors will be unchanged.  And we will store the values 
        in a new list called revisedRGB.
        """
        for item in imgData:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                revisedRGB.append((255, 255, 255, 0))
            else:
                revisedRGB.append(item)
        
        rgba.putdata(revisedRGB)
        
        # Save out the results
        out = "digit_" + str(count) + ".png"
        count = count +1
        rgba.save(out,"PNG")






    