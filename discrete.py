from colour import Color

import common


def __discrete_color_fun(element):
    return element


def __get_dict_colors(uniq_elems, colors=None):
    if colors is None:
        colors = (Color('black'), Color('yellow'))

    color_range = list(colors[0].range_to(colors[1], len(uniq_elems) + 1))
    dict_colors = {}
    for ip, color in zip(uniq_elems, color_range):
        dict_colors[ip] = common.get_rgb_tuple(color)

    return dict_colors


def get_picture(data, curve_mode, size=None, max_len=None, colors=None):
    dict_colors = __get_dict_colors(list(set(data)), colors)

    if curve_mode == 'hilbert':
        p = common.get_hilbert_p(max_len)
        xy_fun = common.get_hilbert_xy(p=p)
        side_len = 2 ** p
        size = (side_len, side_len)

    elif curve_mode == 'morton':
        xy_fun = None  # TODO add morton curve mode
    else:  # horizontal
        width, height = size
        xy_fun = common.get_horizontal_xy(width)

        if max_len is None:
            max_len = width * height

    return common.final_get_pict(data=data, size=size, max_len=max_len,
                                 xy_fun=xy_fun, color_fun=__discrete_color_fun, dict_colors=dict_colors)
