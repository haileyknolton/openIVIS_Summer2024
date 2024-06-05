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
from createBayerImage import save_bayer

# Function to save images as png's
def save_image(expName, filePath, color,level,onTime):
    imgPath = filePath + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
        
    levelStr = "{:.2f}".format(level)
    timeStr = "{:.2f}".format(onTime)
    imgName = imgPath + expName + "_" + color + "_" + levelStr + "_" + timeStr + ".png"
    #subprocess.run(["libcamera-still","-e","png","-o",imgName])
    subprocess.run(["libcamera-still","-e","png","--autofocus-mode", "auto", "--shutter", str(int(onTime*1_000_000)),"-o",imgName])



# Pixel Variable
pin = board.D18    # Pin connected to the Data In of the NeoPixel strip
num = 8            # The number of NeoPixels
order = neopixel.RGBW # The order of the pixel colors (RGBW or GRBW)
level = 1.0
pixels = neopixel.NeoPixel(pin, num, brightness=level, auto_write=False, pixel_order=order)
   
# Main Function
# Ask user to cyle colors
while True:
    try:
        loopColors = int(input("Cyle through colors (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if loopColors < 0 or loopColors > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# If not cycling colors ask for color value
if loopColors == 0:
    while True:
        try:         
            selectColor = int(input("Enter Desired Colors (Green = 1, Red = 2, Blue = 3, White = 4): "))
        except ValueError:
            print("Invalid Entry. Try again")
            continue
        if loopColors < 0 or loopColors > 4:
            print("Invalid Entry. Try again")
            continue
        else:
            break

# Ask user to cyle brightness levels
while True:
    try:
        loopLevels = int(input("Cyle through brightness levels (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if loopLevels < 0 or loopLevels > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# If not cycling brightness ask for brightness value
if loopLevels == 0:
    while True:
        try:         
            selectLevel = float(input("Enter Desired Brightness (Min = 0, Max = 1): "))
        except ValueError:
            print("Invalid Entry. Try again")
            continue
        if selectLevel < 0 or selectLevel > 1:
            print("Invalid Entry. Try again")
            continue
        else:
            break

# Ask user for LED on time
while True:
    try:
        onTime = float(input("Set LED On Time (secs): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if onTime < 0:
        print("Invalid Entry. Try again")
        continue
    else:
        break
 

# Ask user to save images
while True:
    try:
        saveImages = int(input("Save Images (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if saveImages < 0 or saveImages > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Ask user to save BAYER
while True:
    try:
        saveBayer = int(input("Save Bayer Images (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if saveImages < 0 or saveImages > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Ask User for Experiment Name
if saveImages:
    while True:
        try:
            expName = input("Enter experiment name: ")
        except expName:
            print("Invalid Entry. Try again")
            continue
        else:
            break

# Ask user for saving directory
while True:
    try:
        defaultPath = int(input("Save to Default Directory? (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if loopColors < 0 or loopColors > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# If not saving to default
if defaultPath == 1:
    filePath = "/home/pi/Downloads/ImagesopenIVIS/"
else:
    while True:
        try:
            filePath = input("Enter Desired Directory: ")
        except filePath:
            print("Invalid Entry. Try again")
            continue
        else:
            break


# Turn off Leds
pixels.fill((0,0,0,0))
pixels.show()

# Set Color Value
if loopColors:
    print("Looping through colors: RGBW")
    for ii in range(1,5):
        if ii == 1:
            color = (0,255,0,0)
            colorStr = "Green"
            print("Starting: Green")
        elif ii == 2:
            color = (255,0,0,0)
            colorStr = "Red"
            print("Starting: Red")
        elif ii == 3:
            color = (0,0,255,0)
            colorStr = "Blue"
            print("Starting: Blue")
        else:
            color = (0,0,0,255)
            colorStr = "White"
            print("Starting: White")

        if loopLevels:
            print("Looping through brightness levels")
            for jj in range(0,11,1):
                print("Brightness: ",jj/10)
                pixels.fill(color)
                pixels.brightness = jj/10
                pixels.show()
                time.sleep(onTime)
                if saveImages:
                    save_image(expName,filePath, colorStr,jj/10,onTime)
                if saveBayer:
                    save_bayer(expName,filePath,colorStr,jj/10, onTime)
        else:
            pixels.fill(color)
            pixels.brightness = selectLevel
            pixels.show()
            time.sleep(onTime)
            if saveImages:
                save_image(expName,filePath,colorStr,selectLevel,onTime)
            if saveBayer:
                save_bayer(expName,filePath,colorStr,selectLevel,onTime)
else:
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
    
    if loopLevels:
        for jj in range(0,11,1):
            pixels.fill(color)
            pixels.brightness = jj/10
            pixels.show()
            time.sleep(onTime)
            if saveImages:
                save_image(expName,filePath,colorStr,jj/10,onTime)
            if saveBayer:
                save_bayer(expName,filePath,colorStr,jj/10,onTime)
    else:
        pixels.fill(color)
        pixels.brightness = selectLevel
        pixels.show()
        time.sleep(onTime)
        if saveImages:
            save_image(expName,filePath,colorStr,selectLevel,onTime)
        if saveBayer:
                save_bayer(expName,filePath,colorStr,selectLevel, onTime)

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()

if saveImages:
    imgPath = filePath + expName + "/"
    subprocess.run(["chown","-R","pi",imgPath])

if saveBayer:
    imgPath = filePath + expName + "/"
    subprocess.run(["chown","-R","pi",imgPath])
