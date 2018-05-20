import pandas as pd

from scripts import discrete, set_colors
from math import sqrt

file_path = 'CSDMC_API_Train.csv'
pict_path = 'pictures/csdmc/'

data = pd.read_csv(file_path, header=None)
width = 32


def get_samples(verdict):
    samples_set = data[data.verdict == verdict]['calls']
    samples = [s.split(' ') for s in samples_set]
    return samples
    pass


def get_calls(samples):
    calls = []
    for s in samples:
        calls += s
    return set(calls)


def get_pict(samples, path, dict_colors):
    for i, s in enumerate(samples):
        l = len(samples[i])
        w = int(sqrt(l))
        h = l / w + 1
        im, leg = discrete.get_picture(data=samples[i], curve_mode='hor',
                                       # max_len=1024,
                                       size=(w, h),
                                       colors=dict_colors)
        im.resize((500, 500)).save(path + 'csdmc' + str(i) + '.png')


def main():
    data.columns = ['verdict', 'calls']
    malwares = get_samples(1)
    harmless = get_samples(0)

    calls = get_calls(malwares + harmless)
    dict_colors = discrete.__get_dict_colors(calls, set_colors.set_colors[4])

    get_pict(malwares, pict_path + 'malw/', dict_colors)
    get_pict(harmless, pict_path + 'harmless/', dict_colors)

    leg = discrete.__get_discr_legend(dict_colors)
    leg.save(pict_path + 'csdmc_leg.png')
    pass


if __name__ == '__main__':
    main()
