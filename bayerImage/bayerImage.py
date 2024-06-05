import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import cv2

fileName = 'save3_white_0.50.png'
filePath = "/home/pi/Downloads/openIVIS-main/Python/Summer24/colors/white5_white_0.50.png"
import cv2
import numpy as np

# Function to convert RGB image to Bayer pattern
def rgb_to_bayer(rgb_image):
    height, width, _ = rgb_image.shape
    bayer_image = np.zeros((height, width), dtype=np.uint8)
    bayer_image[0:height:2, 0:width:2] = rgb_image[0:height:2, 0:width:2, 2]  # Red
    bayer_image[0:height:2, 1:width:2] = rgb_image[0:height:2, 1:width:2, 1]  # Green
    bayer_image[1:height:2, 0:width:2] = rgb_image[1:height:2, 0:width:2, 1]  # Green
    bayer_image[1:height:2, 1:width:2] = rgb_image[1:height:2, 1:width:2, 0]  # Blue
    return bayer_image

# Read the RGB image
rgb_image = cv2.imread(filePath)

if rgb_image is None:
    raise ValueError("Image not found or unable to load the image.")

# Convert the RGB image to Bayer pattern
bayer_image = rgb_to_bayer(rgb_image)

# Save the Bayer image as a .npy file
np.save('bayerWhite5.npy', bayer_image)

print("Bayer image saved as 'bayer_image.npy'")

