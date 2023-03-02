import numpy as np
from PIL import Image
import matplotlib.cm as cm

# Load the RGB image
rgb_image = np.array(Image.open('rgb_image.tif'))

# Extract the red and green channels
red_channel = rgb_image[:,:,0]
green_channel = rgb_image[:,:,1]

# Calculate GNDVI values
gndvi_values = np.divide((green_channel - red_channel), (green_channel + red_channel))

# Define the range of GNDVI values and corresponding colors
gndvi_ranges = [(0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0)]
gndvi_colors = ['red', 'orange', 'yellow', 'green', 'blue']

# Create a color map for the GNDVI ranges
cmap = cm.colors.ListedColormap(gndvi_colors)

# Calculate the corresponding color for each pixel based on GNDVI range
gndvi_indices = np.searchsorted([r[1] for r in gndvi_ranges], gndvi_values)
gndvi_indices = np.clip(gndvi_indices, 0, len(gndvi_ranges)-1)
colors = cmap(gndvi_indices)

# Create a new RGB image with the GNDVI range colors
false_color_image = np.dstack((colors[:,:,0], colors[:,:,1], colors[:,:,2]))

# Save the new RGB image as a JPEG
false_color_image = Image.fromarray(np.uint8(false_color_image*255))
false_color_image.save('false_color_map.jpeg')
