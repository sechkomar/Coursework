import pandas as pd
import matplotlib.pyplot as plt
import mpldatacursor

from scripts import discrete, set_colors, continuous, common

folder_path = "D:\coursework\VizSec\spam\\"
# folder_path = ''

pict_path = 'pictures/'
# pict_path = 'D:\coursework\pictures\\'

filename = 'spam.csv'

orig_spam_data = pd.read_csv(folder_path + filename)

p = 7
max_len = 4 ** p
size = 2 ** p

rand_spam_data = (orig_spam_data.sample(n=max_len, random_state=47)).sort_values(by='Unnamed: 0')
rand_spam_data.time = pd.to_datetime(rand_spam_data.time)

# print(rand_spam_data)

hilbert_xy = common.get_hilbert_xy(p)
plot_xy = [hilbert_xy(i) for i in range(0, max_len)]
serial = {tuple(coord): i for i, coord in enumerate(plot_xy)}


def segment_id(extremum_values, num_of_steps, value):
    min_el, max_el = extremum_values
    step = (max_el - min_el) / float(num_of_steps)

    if value == max_el:
        return num_of_steps - 1
    return int((value - min_el) / float(step))


hours = [time.hour for time in rand_spam_data.time]
durations = [d for d in rand_spam_data['duration']]

source_ports = [p for p in rand_spam_data['source_port']]
dest_ports = [p for p in rand_spam_data['dest_port']]

flags = [f for f in rand_spam_data['tsp_flags']]

with open('..\dest_ip_countries.txt', 'r') as fin:
    dest_countries = [l.strip('\n') for l in fin.readlines()][:max_len + 1]
with open('..\source_ip_countries.txt', 'r') as fin:
    src_countries = [l.strip('\n') for l in fin.readlines()][:max_len + 1]

all_countries = {c: i for i, c in enumerate(set(dest_countries + src_countries))}
names_by_id = {i: c for c, i in all_countries.items()}

dest_cont_ids = [all_countries[c] for c in dest_countries]
src_cont_ids = [all_countries[c] for c in src_countries]

packets = [int(p) for p in rand_spam_data['packets_sent']]

columns = ['time', 'src country', 'dest country', 'duration', 'packets_sent']
data = {
    c: l for c, l in zip(columns, [hours, src_cont_ids, dest_cont_ids, durations, packets])
}

other_names = ['src country', 'dest country']

cols = 3
rows = len(data) / cols + (1 if len(data) % cols != 0 else 0)


def xy_by_plot(x, y):
    col = int(x + 0.5)
    row = int(y + 0.5)
    return col, row


def onclick(event):
    x, y = xy_by_plot(event.xdata, event.ydata)
    ord_id = serial[(x, y)]

    info_fig = plt.figure(figsize=(2, 2))

    info_ax = info_fig.add_subplot(111)
    info_fig.canvas.toolbar.pack_forget()
    info_fig.canvas.set_window_title('Element info')
    info_ax.set_yticklabels([])
    info_ax.set_xticklabels([])
    info_ax.axis('off')

    info_ax.text(0, 0, infos[ord_id], family='sans-serif')
    info_fig.show()
    pass


import numpy as np

# figure = plt.figure()
# figure.canvas.set_window_title('Pixel plot')
for ii, key in enumerate(data):
    vals = data[key]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.canvas.set_window_title('Pixel plot')
    # ax = figure.add_subplot(rows, cols, ii + 1)
    ax.set_title(key)


    def form_coord(x, y):
        x_p, y_p = xy_by_plot(x, y)
        ser = serial[(x_p, y_p)]
        return 'x={}, y={}, serial={}'.format(x_p, y_p, ser)


    im_list = np.zeros((size, size))

    for jj, coord in enumerate(plot_xy):
        v = vals[jj]
        im_list[coord[0]][coord[1]] = v

    ax.format_coord = form_coord
    im = ax.imshow(im_list, cmap='plasma')
    # colorbar = figure.colorbar(im)
    colorbar = fig.colorbar(im)
    if key in other_names:
        # colorbar.set_ticks(st)
        colorbar.ax.set_yticklabels([names_by_id[c] for c in set(vals)])
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    pass

infos = ['serial_num = {}\n'.format(ord_id)
         + 'x={}, y={}\n'.format(*plot_xy[ord_id])
         + '\n'.join(['{}={}'.format(feat, val[ord_id]) for feat, val in data.items()])
         for ord_id in range(0, max_len)]


def cursor_info(**kwargs):
    i = int(kwargs['i'])
    j = int(kwargs['j'])
    ord_id = int(serial[(i - 1, j - 1)])
    return 'serial = {}'.format(ord_id)


# mpldatacursor.datacursor(hover=True, bbox=dict(alpha=0.7, fc='w'),
#                          formatter=cursor_info)
# cid = figure.canvas.mpl_connect('button_press_event', onclick)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
