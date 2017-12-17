import pandas as pd
from os import listdir
import random

desired_size = 4 ** 7

folder_path = "/media/sechko/D814F3AB14F38AB0/coursework/VizSec/spam/"
columns = ['time', 'duration', 'source_ip', 'dest_ip', 'source_port', 'dest_port',
           'protocol', 'tsp_flags', 'tos', 'smth', 'packets_sent', 'bytes_sent', 'verdict']

conc_file = 'spam.csv'


def read_random_from_csv(path, size, header):
    num_lines = sum(1 for l in open(path))
    skip_idx = []
    if num_lines > size:
        skip_idx = random.sample(range(0, num_lines), num_lines - size - 1)
    data = pd.read_csv(path, skiprows=skip_idx, header=header)
    # print data.head()
    return data


def concatenate():
    # folder_path = "spam\\"
    data = []
    files = [f for f in sorted(listdir(folder_path))]
    for file in files:
        file_path = folder_path + file
        curr_data = read_random_from_csv(file_path, 4 ** 5 + 800, None)
        data.append(curr_data)

    result = pd.concat(data)

    result.columns = columns
    result.to_csv(folder_path + conc_file)


def get_small_file(size):
    data = read_random_from_csv(folder_path + conc_file, size, None)
    # data.columns = columns
    data.to_csv(folder_path + 'small.csv')


if __name__ == '__main__':
    concatenate()
    # get_small_file(4 ** 7)
    pass
