
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Define the pixel coordinates you are interested in
pixel_x = 1430  # Example x-coordinate
pixel_y = 2050   # Example y-coordinate

name='intTest5'
# List of file paths to the images taken at different exposure times
#image_files = [name+'1.png', name+'2.png', name+'3.png', name+'4.png']#, name+'5.png']

# Corresponding exposure times (in seconds, for example)
exposure_times = [.001,.005,.01,.02,.04,.06,.08,0.1]#[1, 2, 4, 8, 16]  # Adjust these according to your data
intensities = []

# Initialize a list to store the pixel intensities
for exp_time in exposure_times:
    image_file = 'intTest5/intTest5_'+"{:.3f}".format(exp_time)+'.png'
    image = Image.open(image_file).convert('L')  # Convert to grayscale
    image_array = np.array(image)
    pixel_intensity = image_array[pixel_y, pixel_x]
    intensities.append(pixel_intensity)


# Loop through each image file and extract the intensity of the target pixel
#for image_file in image_files:
#    image = Image.open(image_file).convert('L')  # Convert to grayscale
#    image_array = np.array(image)
#    pixel_intensity = image_array[pixel_y, pixel_x]
#    intensities.append(pixel_intensity)

# Plot the intensity vs. exposure time
plt.figure(figsize=(10, 6))
plt.plot(exposure_times, intensities, marker='o', color='black')
plt.title('Pixel Intensity vs. Exposure Time')
plt.xlabel('Exposure Time (s)')
plt.ylabel('Pixel Intensity')
plt.grid(True)

plt.savefig("Intensity_vs_Exposure_" + name +".png")
plt.show()

#FOR HISTOGRAM

image_path = 'intTest5/intTest5_0.010.png'  # Replace with your image path
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_array = np.array(image)

# Flatten the image array to get the intensity values
intensity_values = image_array.flatten()

# Plot the histogram of pixel intensities
plt.figure(figsize=(10, 6))
plt.hist(intensity_values, bins=256, range=(0, 255), color='black', alpha=0.75)
plt.title('Pixel Intensity Histogram '+ image_path)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig("Pixel Intensity Histogram_" + name + "0.010.png")
plt.show()
