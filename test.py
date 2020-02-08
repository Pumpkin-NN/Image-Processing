import skimage
from skimage import data
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

camera_man = data.camera()
'''
# Use PIL show the image
img = Image.fromarray(camera_man)
img = img.show()
'''

# Use plt show the image
plt.imshow(camera_man, 'gray')
# Show the image on console
plt.show()

