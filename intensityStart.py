# Last Updated 5/29/24

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
from matplotlib import image
import cv2

def save_image(expName, filePath,expTime):
    imgPath = filePath + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
   
    expStr = "{:.3f}".format(expTime)
    imgName = imgPath + expName + "_" + expStr + ".png"
    #subprocess.run(["libcamera-still","-e","png","-o",imgName])
    subprocess.run(["libcamera-still","-e","png","--autofocus-mode", "auto", "--shutter", str(int(expTime*1000000)),"-o",imgName])


# Pixel Variable
pin = board.D18    # Pin connected to the Data In of the NeoPixel strip
num = 8            # The number of NeoPixels
order = neopixel.RGBW # The order of the pixel colors (RGBW or GRBW)
level = 1.0
pixels = neopixel.NeoPixel(pin, num, brightness=level, auto_write=False, pixel_order=order)
   
# Main Function
# Ask user to cyle colors
selectColor=4

# Ask for brightness value
selectLevel=0.5

# Ask user for LED on time
onTime=1
        
loopTime = 1


# Ask user to save images
saveImages = 1


# Ask User for Experiment Name
expName = "intTest5"

# Ask user for saving directory

filePath = "/home/pi/Downloads/openIVIS-main/Python/Summer24/"


# Turn off Leds
pixels.fill((0,0,0,0))
pixels.show()

# Set Color Value

if selectColor == 1:
	color = (0,255,0,0)
	colorStr = "Green"
elif selectColor == 2:
	color = (255,0,0,0)
	colorStr = "Red"
elif selectColor == 3:
	color = (0,0,255,0)
	colorStr = "Blue"
else:
	color = (0,0,0,255)
	colorStr = "White"


jj = [0.001,0.005,0.01,0.02,0.04,0.06,0.08,0.1]

print("Looping through exposure times")
for i in jj:
	print("Exposure Time: ",i)
	pixels.fill(color)
	pixels.brightness = selectLevel
	pixels.show()
	time.sleep(onTime)
	if saveImages:
		save_image(expName,filePath, i)
	


# Turn off Leds
pixels.fill((0,0,0))
pixels.show()

if saveImages:
    imgPath = filePath + expName + "/"
    subprocess.run(["chown","-R","pi",imgPath])

