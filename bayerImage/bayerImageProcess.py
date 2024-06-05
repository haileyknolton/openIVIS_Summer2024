
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the Bayer pattern data from a .npy file
fileName = 'bayerWhite5'
bayer_data = np.load(fileName+'.npy')

# Display the Bayer pattern data
plt.imshow(bayer_data, cmap='gray')
plt.title('Bayer Pattern Image')
plt.colorbar()
plt.show()

cv2.imwrite('gray'+fileName+'.png',bayer_data)
