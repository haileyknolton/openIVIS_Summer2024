import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the Bayer pattern data from a .npy file
bayer_data = np.load('bayer_image.npy')

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
cv2.imwrite('colorized_bayer_image.png', cv2.cvtColor(colorized_bayer, cv2.COLOR_RGB2BGR))
