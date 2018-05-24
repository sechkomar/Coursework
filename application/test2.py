import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor
import pandas as pd
from random import shuffle
from matplotlib.colors import Colormap

np.random.seed(777)

width, height = 50, 50
samples_count = width * height
features_count = 6

data = {'feature_{}'.format(i): np.array([np.array(np.random.binomial(10, 0.87, width))
                                          for k in range(0, height)]) for i in range(0, features_count)}

# a = np.array(np.random.binomial(10, 0.87, width))
# print(type(a), a)

xy_by_i = {}
i_by_xy = np.zeros((height, width), dtype=int)


def init_data():
    order = list(range(0, samples_count))
    shuffle(order)
    for i in range(0, height):
        for j in range(0, width):
            order_id = order[i * width + j]

            xy_by_i[order_id] = (i, j)
            i_by_xy[i][j] = order_id

    return xy_by_i


def row_data():
    d = {
        k: [v[xy_by_i[i]] for i in range(0, samples_count)]
        for k, v in data.items()
    }
    return pd.DataFrame(d)


init_data()
raw = row_data()

cols = 3
rows = len(data) / cols + (1 if len(data) % cols != 0 else 0)

colorFrom = ''
colorTo = ''
with open('color.txt', 'r') as fin:
    colorFrom, colorTo = fin.readline().split(' ')

cmap = Colormap('current')
# cmap.set_over(color=colorFrom)
# cmap.set_under(color=colorTo)


figure = plt.figure()


def xy_by_plot(x, y):
    col = int(x + 0.5)
    row = int(y + 0.5)
    return col, row


for i, key in enumerate(data):
    vals = data[key]
    ax = figure.add_subplot(rows, cols, i + 1)
    ax.set_title(key)


    def form_coord(x, y):
        return 'x={}, y={}'.format(*xy_by_plot(x, y))


    ax.format_coord = form_coord
    im = ax.imshow(vals)

infos = ['serial_num = {}\n'.format(ord_id)
         + 'x={}, y={}\n'.format(*xy_by_i[ord_id])
         + '\n'.join(['{}={}'.format(col, raw.loc[ord_id, col]) for col in raw])
         for ord_id in range(0, samples_count)]


def cursor_info(**kwargs):
    i = int(kwargs['i'])
    j = int(kwargs['j'])
    ord_id = int(i_by_xy[i - 1, j - 1])
    return 'serial_num={}'.format(ord_id)


mpldatacursor.datacursor(hover=True, bbox=dict(alpha=0.7, fc='w'),
                         formatter=cursor_info)

figure.subplots_adjust(right=0.8)
cbar_ax = figure.add_axes([0.85, 0.15, 0.05, 0.7])
figure.colorbar(im, cax=cbar_ax)


def onclick(event):
    x, y = xy_by_plot(event.xdata, event.ydata)
    ord_id = i_by_xy[x][y]

    # print(infos[ord_id])

    info_fig = plt.figure(figsize=(1.5, 1.5))
    info_ax = info_fig.add_subplot(111)
    info_fig.canvas.toolbar.pack_forget()

    info_ax.set_yticklabels([])
    info_ax.set_xticklabels([])
    info_ax.axis('off')

    info_ax.text(0, 0, infos[ord_id], family='serif')
    info_fig.show()
    # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       ('double' if event.dblclick else 'single', event.button,
    #        event.x, event.y, event.xdata, event.ydata)
    #       )


cid = figure.canvas.mpl_connect('button_press_event', onclick)

plt.show()
