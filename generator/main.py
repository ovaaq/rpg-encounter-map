# -*- coding: utf-8 -*-
# Author: Paavo Koivistoinen
# Telegram: https://t.me/ovaaq

from PIL import Image

from generator.utility import add_object_to_image

im1 = Image.open("../assets/Textures - 300 DPI/Texture - Mossy Floor - Green 1.jpg")

im2 = Image.open("../assets/Assets - 300 DPI/Bush 6 - Green 3.png")


tmp = add_object_to_image(im1, im2, rotate_degrees=0, scale=1)
tmp.show()
