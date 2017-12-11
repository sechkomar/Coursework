import common
from colour import Color


def __get_list_colors(num_of_steps, colors=None):
    if colors is None:
        colors = (Color('black'), Color('yellow'))

    color_range = list(colors[0].range_to(colors[1], num_of_steps))
    color_list = [common.get_rgb_tuple(color) for color in color_range]
    return color_list


def __get_cont_color_fun(extremum_values, num_of_steps):
    min_el, max_el = extremum_values
    step = (max_el - min_el) / float(num_of_steps)

    def cont_color_fun(value): #TODO do not so govnocode
        if (value == max_el):
            return num_of_steps - 1
        return int((value - min_el) / float(step))  # float() is necessary?

    return cont_color_fun


def get_picture(data, curve_mode, num_of_steps, size=None, max_len=None, colors=None):
    dict_colors = __get_list_colors(num_of_steps, colors)

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

    color_fun = __get_cont_color_fun((min(data), max(data)), num_of_steps)

    return common.final_get_pict(data=data, size=size, max_len=max_len,
                                 xy_fun=xy_fun, color_fun=color_fun, dict_colors=dict_colors)
