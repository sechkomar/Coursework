import pandas as pd

folder_path = "/media/sechko/D814F3AB14F38AB0/coursework/VizSec/spam/"
pict_path = 'pictures/'
filename = 'spam.csv'

# spam_data = pd.read_csv(folder_path + filename, index_col=False)
# spam_data.drop('Unnamed: 0', axis=1, inplace=True)

# spam_data.time = pd.to_datetime(spam_data.time)

# print(spam_data.columns.values)

# cont = ['time', 'duration', 'source_ip', 'dest_ip', 'source_port', 'dest_port', 'packets_sent', 'bytes_sent']
# descr = ['protocol', 'tsp_flags', 'tos', 'smth', 'verdict']

# cols_num = len(spam_data.columns.values)

# subplots_cols = 5
# subplots_rows = cols_num / subplots_cols + 1

# from scripts.common import *
# from scripts import common
#
#

# def fun(curve_mode, data_len):
#     if curve_mode == 'hilbert':
#         p = common.get_hilbert_p(data_len)
#         xy_fun = common.get_hilbert_xy(p=p)
#         side_len = 2 ** p
#         size = (side_len, side_len)
#
#     else:  # horizontal
#         from math import sqrt
#         width = sqrt(data_len),
#         height = data_len / width + 1
#         size = (width, height)
#         xy_fun = common.get_horizontal_xy(width)
#
#     return size, xy_fun
#
#
# for col in spam_data:
#     if col in cont:
#         pass
#     elif col in descr:
#         pass
#     pass



