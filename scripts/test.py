import pandas as pd

from scripts import continuous


def main():
    path = 'blacklist_flows_cut.csv'

    data = pd.read_csv(path, header=None, nrows=20000 + 32 ** 2)
    print(data.head())
    data = data[20000:] 
    first_ips = [int((ip.split('.'))[0]) for ip in data[3]]

    # ips_hilbert = discrete.get_picture(data=first_ips, curve_mode='hilbert', max_len=32 ** 2)
    # ips_hilbert.resize((500, 500)).save('hilb.png')
    #
    # ips_hor = discrete.get_picture(data=first_ips, curve_mode='hor', size=(32, 32),
    #                                   colors=(Color('black'), Color('red')))
    # ips_hor.resize((500, 500)).save('hor.png')

    ips_cont_hor = continuous.get_picture(data=first_ips, curve_mode='hor', size=(32, 32), num_of_steps=5)
    ips_cont_hor.resize((500, 500)).save('cont_hor.png')

    # ips_cont_hilb = continuous.get_picture(data=first_ips, curve_mode='hilbert', max_len=32 ** 2,
    #                                        num_of_steps=5, colors=(Color('black'), Color('red')))
    #
    # ips_cont_hilb.resize((500, 500)).save('cont_hilb.png')


if __name__ == '__main__':
    main()
