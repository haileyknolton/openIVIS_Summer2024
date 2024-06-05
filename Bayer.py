import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import cv2

fileName = 'green4'
saveName1 = fileName + ".png"
filePath = "/home/pi/Downloads/openIVIS-main/Python/Summer24/colors/"+ saveName1


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
saveName2 = "Bayer" + fileName + ".npy"
np.save(saveName2, bayer_image)



# Load the Bayer pattern data from a .npy file
bayer_data = np.load(saveName2)

# Display the Bayer pattern data
plt.imshow(bayer_data, cmap='gray')
plt.title('Bayer Pattern Image')
plt.colorbar()
plt.show()

cv2.imwrite('grayBayer'+fileName+'.png',bayer_data)


# Function to colorize the Bayer pattern
def colorize_bayer_pattern(bayer_data):
    height, width = bayer_data.shape
    
    # Create an empty 3-channel (RGB) image
    colorized_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Assign colors based on Bayer pattern positions (assuming RGGB pattern)
    colorized_image[0:height:2, 0:width:2, 0] = bayer_data[0:height:2, 0:width:2]  # Red
    colorized_image[0:height:2, 1:width:2, 1] = bayer_data[0:height:2, 1:width:2]  # Green
    colorized_image[1:height:2, 0:width:2, 1] = bayer_data[1:height:2, 0:width:2]  # Green
    colorized_image[1:height:2, 1:width:2, 2] = bayer_data[1:height:2, 1:width:2]  # Blue
    
    return colorized_image

# Create the colorized Bayer pattern image
colorized_bayer = colorize_bayer_pattern(bayer_data)

# Display the colorized Bayer pattern image
plt.imshow(colorized_bayer)
plt.title('Bayer Pattern Image')
plt.colorbar()
plt.show()
cv2.imwrite('colorized' + fileName + ".png", cv2.cvtColor(colorized_bayer, cv2.COLOR_RGB2BGR))
