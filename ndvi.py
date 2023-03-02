import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
Image.MAX_IMAGE_PIXELS = None
# Load the RGB image
rgb_image = np.array(Image.open('Orthomosaic_Field3.tif'))

# Extract the red and green channels
red_channel = rgb_image[:,:,0]
green_channel = rgb_image[:,:,1]
blue_channel = rgb_image[:,:,2]

# Calculate GNDVI values
try:
    gndvi_values = np.divide((green_channel - red_channel), (green_channel + red_channel))

# Estimate NIR values from GNDVI
    nir_values = np.divide(gndvi_values + 1, gndvi_values - 1)
    print(nir_values)
# Create a new RGB image with the NIR values substituted for the red channel
    nir_image = np.dstack((nir_values, green_channel, blue_channel))

# Save the new RGB image as a JPEG
    nir_image = Image.fromarray(np.uint8(nir_image*255))
    nir_image.save('nir_image_Field3.tif')
    grey_img=nir_image.convert("L")
    plt.imshow(grey_img,cmap='gray')
    plt.colorbar()
    plt.savefig("NIR_grey_Field3.tif")
except ZeroDivisionError:
    pass