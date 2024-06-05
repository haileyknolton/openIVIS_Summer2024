import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import cv2


# Function to convert RGB image to Bayer pattern
def rgb_to_bayer(rgb_image):
    height, width, _ = rgb_image.shape
    bayer_image = np.zeros((height, width), dtype=np.uint8)
    bayer_image[0:height:2, 0:width:2] = rgb_image[0:height:2, 0:width:2, 2]  # Red
    bayer_image[0:height:2, 1:width:2] = rgb_image[0:height:2, 1:width:2, 1]  # Green
    bayer_image[1:height:2, 0:width:2] = rgb_image[1:height:2, 0:width:2, 1]  # Green
    bayer_image[1:height:2, 1:width:2] = rgb_image[1:height:2, 1:width:2, 0]  # Blue
    return bayer_image


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

# Function to save Bayer Grayscale 
def save_bayer(expName,filePath,color,level,onTime):
    
    imgPath = filePath + expName + "/"
    dirExists = os.path.exists(imgPath)

    rgb_image = cv2.imread(filePath)

    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])

    levelStr = "{:.2f}".format(level)
    timeStr = "{:.2f}".format(onTime)
    imgName = imgPath + expName + "_" + color + "_" + levelStr + "_" + timeStr + ".png"

    rgb_image = cv2.imread(imgName)

    if rgb_image is None:
        raise ValueError("Image not found or unable to load the image.")

    # Convert the RGB image to Bayer pattern
    bayer_image = rgb_to_bayer(rgb_image)

    # Save the Bayer image as a .npy file
    saveBayer = imgName[:-3] + "_" + "Bayer" + ".npy"
    #np.save(saveBayer, bayer_image)
    np.save(os.path.join(imgPath, saveBayer), bayer_image)

    # Load the Bayer pattern data from the .npy file
    bayer_data = np.load(saveBayer)
    # Display the Bayer pattern data
    #plt.imshow(bayer_data, cmap='gray')
    #plt.title('Bayer Pattern Image')
    #plt.colorbar()
    #plt.show()

    #cv2.imwrite(imgName[:-3] + "BayerGRAY" + '.png',bayer_data)
    cv2.imwrite(os.path.join(imgPath , imgName[:-3] + "_" + "BayerGRAY" + '.png'), bayer_data)
 

    # Create the colorized Bayer pattern image
    colorized_bayer = colorize_bayer_pattern(bayer_data)

    # Display the colorized Bayer pattern image
    #plt.imshow(colorized_bayer)
    #plt.title('Bayer Pattern Image')
    #plt.colorbar()
    #plt.show()
    
    cv2.imwrite(os.path.join(imgPath , imgName[:-3] + "_" + "BayerCOLOR" + '.png'), cv2.cvtColor(colorized_bayer, cv2.COLOR_RGB2BGR))



