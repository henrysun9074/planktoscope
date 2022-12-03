from typing import Any, List
import numpy as np
import pandas as pd
from skimage import data, io
from skimage.util import img_as_float
from matplotlib import pyplot as plt
import PIL
import scipy.ndimage as ndi
from morphocut import image

# Modify for future use

# class ImageFile:
#     """ Image File class to save file path, file name, date, """

#     def __init__(self, filename):
#         self.path = filename
#         self.image_name = filename.split("\\")[-1]
#         self.date = self.get_date()
#         self.mm, self.dd, self.yy = self.date.split("/")
#         self.mask_id = None

#     def read_img_orig(self):
#         """
#         reads image path and returns original image(np.array)
#         """
#         return np.asarray(Image.open(self.path))

#     def read_img_sliced(self):
#         """
#         reads image path and returns sliced image(np.array) for faster display
#         select every other row and columns and return sliced image
#         """
#         img = self.read_img_orig()
#         return img[::2, ::2]

image = io.imread("imgs/Ff2imKpXkAAwwg1.jpeg")
image = image[:, :, ::-1]
# image = img_as_float(image)
io.imshow(image)
plt.show()
# print(image)


