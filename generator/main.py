# -*- coding: utf-8 -*-
# Author: Paavo Koivistoinen
# Telegram: https://t.me/ovaaq

from PIL import Image

im1 = Image.open("../assets/Textures - 300 DPI/Texture - Mossy Floor - Green 1.jpg")

im2 = Image.open("../assets/Assets - 300 DPI/Bush 6 - Green 3.png")

resizedImage = im2.resize((40, 40))


im1.paste(resizedImage, (400, 400), resizedImage)

im1.show()
