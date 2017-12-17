from PIL import Image, ImageFont
import imp
from math import ceil
from numpy import log2

hilbert = imp.load_source('h', 'hilbert_curve/hilbert.py')

legend_width = 30

def get_rgb_tuple(color):
    return tuple([int(ci * 256) for ci in color.get_rgb()])


def get_hilbert_p(max_len):
    return int(ceil(log2(max_len) / 2))


def get_hilbert_xy(p):
    def hilbert_xy(i):
        return hilbert.coordinates_from_distance(N=2, h=i, p=p)

    return hilbert_xy


def get_horizontal_xy(width):
    def horizontal_xy(i):
        return i % width, int(i / width)

    return horizontal_xy


def final_get_pict(data, size, max_len, xy_fun, color_fun, dict_colors=None):
    im = Image.new(mode='RGB', size=size, color='white')

    for i, elem in enumerate(data):
        xy_ = xy_fun(i)
        idx = color_fun(elem)
        color = dict_colors[idx]
        im.putpixel(value=color, xy=xy_)

        if i == max_len - 1:
            break

    return im



# def get_color_fun(data_type, extremum_elements=None, num_of_steps=None):
#     if data_type == 'c':
#         min_el, max_el = extremum_elements
#         step = (max_el - min_el) / float(num_of_steps)
#
#         def contin_color_fun(value):
#             return int((value - min_el) / step)
#
#         return contin_color_fun
#
#     else:  # 'd'
#         def discr_color_fun(value):
#             return value
#
#         return discr_color_fun
