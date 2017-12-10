from colour import Color
from PIL import Image
import numpy as np

import imp

hilbert = imp.load_source('h', 'hilbert_curve/hilbert.py')


def get_pict(data, size, location_fun, dict_colors=None):

    if dict_colors is None:
        dict_colors = get_range_colors(list(set(data)))

    width, height = size
    im = Image.new(mode='RGB', size=size, color='green')

    for i, elem in enumerate(data):
        xy_ = location_fun(i)
        im.putpixel(value=dict_colors[elem], xy=xy_)

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


def get_horizontal_line_pict(data, size, dict_colors=None):

    width, height = size

    def get_xy(i):
        return (i % width, i / width)

    return get_pict(data, size, get_xy, dict_colors)

def get_hilbert_pic(data, max_len, dict_colors=None):

    p = int(np.log2(max_len) / 2) + 1
    side_len = 2 ** p

    def hilbert_xy(i):
        return hilbert.coordinates_from_distance(N=2, h=i, p=p)

    return get_pict(data, (side_len, side_len),  hilbert_xy, dict_colors)
