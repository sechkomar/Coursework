from colour import Color
from PIL import Image


def get_horizontal_line_pict(data, size, num_of_steps, colors=(Color('black'), Color('yellow'))):
    width, height = size
    color_from, color_to = colors

    colors = list(color_from.range_to(color_to, num_of_steps + 1))

    min_el = min(data)
    step = (max(data) - min_el) / float(num_of_steps)

    def get_color_index(value):
        return int((value - min_el) / step)

    im = Image.new(mode='RGB', size=size, color='green')

    for i, elem in enumerate(data):
        color_id = get_color_index(elem)
        im.putpixel(value=colors[color_id], xy=(i % width, i / width))

        if i == width * height - 1:
            break

    return im
