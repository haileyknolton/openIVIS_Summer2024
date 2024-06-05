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
num = 1            # The number of NeoPixels
order = neopixel.RGBW # The order of the pixel colors (RGBW or GRBW)
level = 1.0
pixels = neopixel.NeoPixel(pin, num, brightness=level, auto_write=False, pixel_order=order)
   
# Main Function
color = ((0,0,0,250))
onTime=1
expTime = 0.01 #exposure time in seconds [0.001,0.01,0.1,1]
selectLevel=0.2
expName = "diffTest4"


# Turn off Leds
pixels.fill((0,0,0,0))
pixels.show()

# Turn on Leds with specified color and brightness
pixels.fill(color)
pixels.brightness = selectLevel
pixels.show()
time.sleep(onTime)
save_image(expName, expTime)

#img = cv2.imread(os.path.join(imgPath,expName)


# Turn off Leds
pixels.fill((0,0,0))
pixels.show()

#imgPath = "/home/pi/Pictures/" + expName + "/"
#subprocess.run(["chown","-R","pi",imgPath])

