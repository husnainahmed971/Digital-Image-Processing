#!/usr/bin/env python
# coding: utf-8

# # Import Libraries:

# In[1]:


import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt


# # Read Image:

# In[2]:


from PIL import Image

# Open an image file
image = Image.open('starryNight.jpg')

# Display the image
image.show()


# In[3]:


import cv2

# Load an image
image = cv2.imread('starryNight.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Image Resolution:

# In[7]:


from PIL import Image

# Open the image file
image = Image.open('starryNight.jpg')

# Set the new resolution (width, height)
new_resolution = (800, 600)

# Resize the image
resized_image = image.resize(new_resolution)

# Convert the image to RGB mode (if it's not already in RGB mode)
if resized_image.mode == 'RGBA':
    resized_image = resized_image.convert('RGB')

# Save the resized image
resized_image.save('resized_image.jpg')

# Display the resized image
resized_image.show()


# # Image Sampling:

# In[10]:


from PIL import Image

# Open the image file
image = Image.open('starryNight.jpg')

# Define the sampling factor
sampling_factor = 2  # Reduce the image resolution by a factor of 2

# Sample the image
sampled_image = image.resize((image.width // sampling_factor, image.height // sampling_factor))

# Convert the image to RGB mode
sampled_image = sampled_image.convert('RGB')

# Save and display the sampled image
sampled_image.save('sampled_image.jpg')
sampled_image.show()


# # Image Quantization:

# In[14]:


from PIL import Image

# Open the image file
image = Image.open('starryNight.jpg')

# Define the number of quantization levels (colors)
quantization_levels = 5  # Reduce the image to 16 colors

# Quantize the image
quantized_image = image.quantize(colors=quantization_levels)

# Convert the image to RGB mode
quantized_image = quantized_image.convert('RGB')

# Save and display the quantized image
quantized_image.save('quantized_image.jpg')
quantized_image.show()


# In[ ]:




