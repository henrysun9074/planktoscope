from typing import Any, List
import numpy as np
import pandas as pd
import skimage.io, skimage.data
from skimage.util import img_as_float
from matplotlib import pyplot as plt
import PIL
import scipy.ndimage as ndi
from morphocut import image
import morphocut.core

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



# img = skimage.io.imread("imgs/Ff2imKpXkAAwwg1.jpeg")
img = image.ImageReader("imgs/Ff2imKpXkAAwwg1.jpeg")
# how to use pipeline? -> can use skimage instead? try 12/8

print(image.ImageStats(img))
image2 = image.ExtractROI(img)
# morphocut.core.Call(ExtractROI, image)
skimage.io.imshow(image2)
plt.show()

# image = image[:, :, ::-1]
# # image = img_as_float(image)
# skimage.io.imshow(image)
# plt.show()
# print(image)


