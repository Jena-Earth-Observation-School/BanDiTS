#test3eteatda

# add shit 2

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:54:54 2019

@author: jonas
"""


import matplotlib.pyplot as plt
import pylab as plt
import numpy as np
import pandas as pd
import skimage
import skimage.filters as filters
from skimage import io
from skimage.io import imread
from skimage.segmentation import felzenszwalb, mark_boundaries
import gdal

"""
df = pd.read_csv("C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/testpivot3EEVH.csv")

print(df.head())

print(df.tail())

x = df['Band']
y = df['VH']
plt.xlabel('Time Series'); plt.ylabel('VH')
plt.plot(x,y)



id = 0

filenames = ["VH"]

#Marlin Pfad
#filename = "C:/Users/marli/Desktop/GEO402_Testdaten/test_1d_" + filenames[id] + ".tif"

#Jonas Pfad
filename = "C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/radar/test_1d_" + filenames[id] + ".tif"

img = imread(filename)

#plt.plot(img)

plt.imshow(img)
plt.show()
"""
"""
# Parameters to twiggle
scale = 1000   # Higher means larger clusters
sigma = 0.5   # Smoothing parameter for Gaussian kernel prior segmentation
min_size = 500 # minimum component size (enforced during processing)

segments_fz = felzenszwalb(img, scale=scale, sigma=sigma, min_size=min_size)

print("Felzenszwalb number of segments: {}".format(len(np.unique(segments_fz))))

plt.imshow(mark_boundaries(img, segments_fz))
plt.show()

"""

#im = io.imread("C:/Users/jonas/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/Ziemer_uebungen/Python/data/radar/test_1d_VH.tif")

im2 = io.imread("C:/Users/jz199/Desktop/S1A_VH_Agulhas_50m_selected_bands_VH.tif", 1)

#print(im.shape)

#print(im[79].shape)
#plt.imshow(im)
#plt.show()
plt.imshow(im2)
plt.show()


"""
with rasterio.open('C:/Users/jonas/Desktop/test_1d_VH.tif', 'r') as ds:
    arr = ds.read()  # read all raster values

print(arr.shape)  # this is a 3D numpy array, with dimensions [band, row, col]
"""
