# -*- coding: utf-8 -*-
# Author: Paavo Koivistoinen
# Telegram: https://t.me/ovaaq

def add_object_to_image(base_image, new_layer, rotate_degrees =0, scale = 1, x=0, y=0):
    """

    :param base_image:
    :param new_layer:
    :param rotate_degrees:
    :param scale:
    :param x:
    :param y:
    :return:
    """
    tmp_image = base_image
    scaled_x = int(new_layer.width*scale)
    scaled_y = int(new_layer.height*scale)
    resized_image = new_layer.resize((scaled_x, scaled_y))
    rotated_image = resized_image.rotate(rotate_degrees)
    tmp_image.paste(resized_image, (x, y), rotated_image)

    return tmp_image
