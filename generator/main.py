# -*- coding: utf-8 -*-
# Author: Paavo Koivistoinen
# Telegram: https://t.me/ovaaq
import matplotlib as matplotlib
from PIL import Image
import matplotlib.pyplot as plt
from generator.utility import add_object_to_image

#im1 = Image.open("../assets/Textures - 300 DPI/Texture - Mossy Floor - Green 1.jpg")

#im2 = Image.open("../assets/Assets - 300 DPI/Foliage 2 - Green 1.png")


#tmp = add_object_to_image(im1, im2, rotate_degrees=0, scale=1)
#tmp.show()

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import shapely.geometry
import shapely.ops

points = np.random.random((100, 2))

vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.show()