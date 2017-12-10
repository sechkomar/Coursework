from colour import Color
from PIL import Image
import numpy as np

import imp

hilbert = imp.load_source('h', 'hilbert_curve/hilbert.py')


def get_pict(data, size, location_fun, dict_colors):
    width, height = size
    im = Image.new(mode='RGB', size=size, color='green')

    for i, elem in enumerate(data):
        im.putpixel(value=dict_colors[elem], xy=location_fun(i))

        if i == width * height - 1:
            break

    return im


def get_rgb_tuple(color):
    return tuple([int(ci * 256) for ci in color.get_rgb()])


def get_range_colors(uniq_elems, colors=(Color('black'), Color('yellow'))):
    color_from, color_to = colors
    colors = list(color_from.range_to(color_to, len(uniq_elems) + 1))
    dict_ip_color = {}
    for ip, color in zip(uniq_elems, colors):
        dict_ip_color[ip] = get_rgb_tuple(color)

    return dict_ip_color


def get_horizontal_line_pict(data, size, colors=(Color('black'), Color('yellow'))):
    width, height = size
    uniq_elems = list(set(data))

    dict_colors = get_range_colors(uniq_elems, colors)

    im = Image.new(mode='RGB', size=size, color='green')

    for i, elem in enumerate(data):
        im.putpixel(value=dict_colors[elem], xy=(i % width, i / width))

        if i == width * height - 1:
            break

    return im


def get_hilbert_pic(data, max_len, colors=(Color('black'), Color('yellow'))):
    uniq_elems = list(set(data))
    dict_colors = get_range_colors(uniq_elems, colors)

    p = int(np.log2(max_len) / 2) + 1
    side_len = 2 ** p
    im = Image.new(mode='RGB', size=(side_len, side_len), color='red')

    for i, elem in enumerate(data):
        xy_ = hilbert.coordinates_from_distance(h=i, N=2, p=p)
        im.putpixel(value=dict_colors[elem], xy=xy_)

        if i == max_len:
            break

    return im
