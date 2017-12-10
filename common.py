from PIL import Image


def get_rgb_tuple(color):
    return tuple([int(ci * 256) for ci in color.get_rgb()])


def get_pict(data, size, max_len, xy_fun, dict_colors=None):
    # if dict_colors is None:
    #     dict_colors = get_dict_colors(list(set(data)))

    im = Image.new(mode='RGB', size=size, color='green')

    for i, elem in enumerate(data):
        xy_ = xy_fun(i)
        im.putpixel(value=dict_colors[elem], xy=xy_)

        if i == max_len:
            break

    return im
