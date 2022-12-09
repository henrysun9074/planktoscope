from typing import Any, List
import numpy as np
import pandas as pd
import skimage.io, skimage.data
from skimage.util import img_as_float
from matplotlib import pyplot as plt
import PIL
import scipy.ndimage as ndi

import os.path
from morphocut import image
from morphocut import Call, Pipeline
from morphocut.contrib.ecotaxa import EcotaxaWriter
from morphocut.contrib.zooprocess import CalculateZooProcessFeatures
from morphocut.file import Glob
from morphocut.image import FindRegions, ImageReader
from morphocut.parallel import ParallelPipeline
from morphocut.str import Format
from morphocut.stream import Enumerate, Unpack

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

with Pipeline() as pipeline:
    img = ImageReader("imgs/Ff2imKpXkAAwwg1.jpeg")
    image.RGB2Gray(img)
pipeline.run()
# skimage.io.imshow(img)
# plt.show

img = skimage.io.imread("imgs/Ff2imKpXkAAwwg1.jpeg")
# print(image.ImageStats(img))
# image2 = image.ExtractROI(img)
# # morphocut.core.Call(ExtractROI, image)
# skimage.io.imshow(image2)
# plt.show()

image = img[:, :, ::-1]
# image = img_as_float(image)
skimage.io.imshow(image)
plt.show()
print(image)


