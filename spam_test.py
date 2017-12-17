import pandas as pd
import discrete
import continuous

from os import listdir
import random

from colour import Color


def read_random(path, size):
    num_lines = sum(1 for l in open(path))
    skip_idx = random.sample(range(1, num_lines), num_lines - size)
    data = pd.read_csv(path, skiprows=skip_idx)
    return data


def main():
    folder_path = "spam\\"
    data = pd.DataFrame()
    for file in listdir(folder_path):
        file_path = folder_path + file
        data.append(other=read_random(file_path, 4 ** 5))

    data.to_csv(path_or_buf='spam.csv')


if __name__ == '__main__':
    main()
