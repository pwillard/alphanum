#!/usr/bin/python
"""Script to generate small bitmaps with white numbers on
an alpha background for reporting marks.
 The output is a set of png files


Basic usage:
$ python3 reportingmark.py  (No file options are needed)

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
Date: June 8, 2023


Well, numbers make sense but you never know, there
is this guy at RailSimStuff.com that puts numbers
on !@#$%^&*() characters.

The TTF font you plan to use does not need to be installed in the system
and it won't know how to use it if it is.
The TTF file *does* need to be in the same folder as the python script.

"""

from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import time
import os

# NOTE: All reporting mark numbers must be the same length
##############################################################################
numberList = "120079","120100","120186","120156"
##############################################################################
# Reporting Mark - Road Name
# If using RailSimStuff fonts, refer to font PDF to know which chars make the
# correct lettering
rm = "NS"
##############################################################################
# Some Setup
elements = len(numberList)
element0 = numberList[0]
len_element0 = len(element0)
len_number = len(numberList)
len_rm = len(rm)

# Gap Size (NOTE: Not all railsimstuff fonts have a *space* character)
# Mileage may vary
space = "  "
len_space = len(space)

# Lettering height and width
height = 64
multiply = len_rm + len_space + len_element0
width = 54 * multiply  # 64 * 10

print ("height = ",height)
print ("width =  ", width)
# You will need to tweak these values below based on the
# specific font being used so it fits the 'box' correctly
fontSize = 68       # Pitch
fontHorz = 20       # Start Position
fontVert = -4       # Start Position
pathToFont = "nslogo.ttf"   # Should be in the local folder where the Script is
fontColor = "255"           # 255 = white


print(pathToFont)

if __name__ == '__main__':

    image = Image.new('RGB', (1024, 1024), (0,0,0))
    image.save('decal.png', 'png')
    image.close()

    # get the font
    #
    fnt = ImageFont.truetype(pathToFont, fontSize)


    #"""
    # Draw Character Black on White Background
    # then invert to White on Black Background (it's just easier)
    # since we can rely on defaults

    #We are looping through each member of the numberList
    #and writing out each character result individually
    #"""

    count = 0

    for elements in numberList:
        output = rm + ' ' + elements
        print (output)
        #Setup
        image = Image.new('RGB', (width, height), (0,0,0))
        draw = ImageDraw.Draw(image)
        #
        draw.text((fontHorz,fontVert),output,font=fnt)

        # Save out the results

        out = str(count) +".png"
        count = count +1

        # Not the most efficient of routines
        # but I'm still designing this next section

        image.save(out,"png")
        image.close()

    img1 = Image.open(r"decal.png") # Create a blank to paste into
    row = 0
    for items in range(count):
        img2 = str(items) + ".png"
        img = Image.open(img2)
        img1.paste(img, (0,row))
        row = row + height

    # Clean up
    for items in range(count):
        img2 = str(items) + ".png"
        time.sleep(2) # GIVE the OS some time to process the file
        os.remove(img2) # remove working copy

    # Save final result and clean up
    img1.save("decalout.png")




