# MIT License
# 
# Copyright (c) 2023 CashLabMines
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import datetime
import board
import neopixel
import os
import subprocess
import numpy as np
from numpy import asarray
from PIL import Image
from matplotlib import pyplot as plt

# Function to save images
def save_image(expName,exposureTime):
    imgPath = "/home/pi/Downloads/openIVIS-main/Python/Summer24/colors/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
    imgName = imgPath + expName + ".png"
    subprocess.run(["libcamera-still","-e","png","--shutter", str(int(exposureTime*1_000_000)),"-o",imgName])
    
    img = Image.open(imgName)
    numpydata = asarray(img)
    #npyname = expName + ".npy"
    #np.save(npyname, numpydata)
    

# Pixel Variable
pin = board.D18    # Pin connected to the Data In of the NeoPixel strip
num = 8            # The number of NeoPixels
order = neopixel.RGBW # The order of the pixel colors (RGBW or GRBW)
level = 1.0
pixels = neopixel.NeoPixel(pin, num, brightness=level, auto_write=False, pixel_order=order)
   
# Main Function
color = ((0,255,0,0))
onTime=1 #exposure time in seconds [0.001,0.01,0.1,1]
selectLevel=0.5
expName = "green4"


# Turn off Leds
pixels.fill((0,0,0,0))
pixels.show()

# Turn on Leds with specified color and brightness
pixels.fill(color)
pixels.brightness = selectLevel
pixels.show()
time.sleep(onTime)
save_image(expName, onTime)
#img = cv2.imread(os.path.join(imgPath,expName)


# Turn off Leds
pixels.fill((0,0,0))
pixels.show()

#imgPath = "/home/pi/Pictures/" + expName + "/"
#subprocess.run(["chown","-R","pi",imgPath])
