import imp
import numpy as np
from colour import Color
from math import ceil
import common

hilbert = imp.load_source('h', 'hilbert_curve/hilbert.py')


def __get_dict_colors(uniq_elems, colors=None):
    if colors == None:
        colors = (Color('black'), Color('yellow'))

    colors = list(colors[0].range_to(colors[1], len(uniq_elems) + 1))
    dict_ip_color = {}
    for ip, color in zip(uniq_elems, colors):
        dict_ip_color[ip] = common.get_rgb_tuple(color)

    return dict_ip_color


def __get_horizontal_pict(data, size, dict_colors=None):
    width, height = size

    def get_xy(i):
        return (i % width, i / width)

    return common.get_pict(data=data, size=size, max_len=width * height, xy_fun=get_xy, dict_colors=dict_colors)


def __get_hilbert_pict(data, max_len, dict_colors=None):
    p = int(ceil(np.log2(max_len) / 2))
    # p = int(np.log2(max_len) / 2)
    side_len = 2 ** p

    def hilbert_xy(i):
        return hilbert.coordinates_from_distance(N=2, h=i, p=p)

    return common.get_pict(data=data, size=(side_len, side_len), max_len=max_len,
                           xy_fun=hilbert_xy, dict_colors=dict_colors)


def get_picture(data, curve_mode, max_len=None, size=None, colors=None):
    dict_colors = __get_dict_colors(list(set(data)), colors)
    if curve_mode == 'hilbert':
        return __get_hilbert_pict(data=data, max_len=max_len, dict_colors=dict_colors)
    elif curve_mode == 'morton':
        return None  # TODO add morton curve mode
    else:  # horizontal
        return __get_horizontal_pict(data=data, size=size, dict_colors=dict_colors)
