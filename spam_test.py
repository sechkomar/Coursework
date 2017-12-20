import pandas as pd

import continuous
import discrete
import set_colors

# folder_path = "/media/sechko/D814F3AB14F38AB0/coursework/VizSec/spam/"
folder_path = ''

# pict_path = 'pictures/'
pict_path = 'D:\coursework\pictures\\'

filename = 'spam.csv'

spam_data = pd.read_csv(folder_path + filename)

columns = ['time', 'duration', 'source_ip', 'dest_ip', 'source_port', 'dest_port',
           'protocol', 'tsp_flags', 'tos', 'smth', 'packets_sent', 'bytes_sent', 'verdict']


def get_hours_picture():
    hours = [time.hour for time in spam_data.time]
    save_discr_pict(data=hours, curve_mode='hilbert', max_len=4 ** 7, dict_colors=set_colors.set_colors[0],
                    path=pict_path + 'hhh')
    # hours_pict, colors = discrete.get_picture(data=hours, curve_mode='hilbert', max_len=4 ** 7,
    #                                           colors=set_colors.set_colors[0])
    # hours_pict.resize((700, 700)).save('pictures/hours.png')
    # colors.save('pictures/hours_legend.png')


def init():
    # print spam_data.head()
    # spam_data.columns = columns
    spam_data.time = pd.to_datetime(spam_data.time)
    pass


def get_duration_pict():
    durations = spam_data['duration']
    # save_cont_pict(data=durations, path=pict_path + 'durations', curve_mode='hilbert',
    #                num_of_steps=50, max_len=4 ** 7, dict_colors=set_colors.set_colors[5])
    dur_pict, dur_legend = continuous.get_picture(data=durations,
                                                  curve_mode='hilbert',
                                                  max_len=4 ** 7,
                                                  num_of_steps=50,
                                                  colors=set_colors.set_colors[5])
    dur_pict.resize((700, 700)).save(pict_path + 'durations.png')
    dur_legend.save(pict_path + 'durations_legend.png')


def save_cont_pict(data, path, curve_mode, num_of_steps, size=None, max_len=None, dict_colors=None):
    pict, legend = continuous.get_picture(data=data,
                                          curve_mode=curve_mode,
                                          num_of_steps=num_of_steps,
                                          size=size,
                                          max_len=max_len,
                                          colors=dict_colors)

    pict.resize((700, 700)).save(path + '.png')
    legend.save(path + '_leg.png')
    pass


def get_ports_pict():
    source_ports = spam_data['source_port']
    dest_ports = spam_data['dest_port']

    steps_num = 10
    dict_colors = continuous.__get_list_colors(steps_num, colors=set_colors.set_colors[7])
    save_cont_pict(source_ports, path=pict_path + 'src_ports', curve_mode='hilbert',
                   num_of_steps=steps_num, max_len=4 ** 7, dict_colors=dict_colors)

    save_cont_pict(dest_ports, path=pict_path + 'dest_ports', curve_mode='hilbert',
                   num_of_steps=steps_num, max_len=4 ** 7, dict_colors=dict_colors)


def get_tcp_flags_pict():
    flags = spam_data['tsp_flags']
    save_discr_pict(data=flags, curve_mode='hilbert', path=pict_path + 'tsp_flags',
                    max_len=4 ** 7,
                    dict_colors=set_colors.set_colors[5])


def save_discr_pict(data, path, curve_mode, size=None, max_len=None, dict_colors=None):
    pict, legend = discrete.get_picture(data=data,
                                        curve_mode=curve_mode,
                                        size=size,
                                        max_len=max_len,
                                        colors=dict_colors)

    pict.resize((700, 700)).save(path + '.png')
    legend.save(path + '_leg.png')

    pass


def get_ips_country():
    with open('dest_ip_countries.txt', 'r') as fin:
        dest_countries = [l.strip('\n') for l in fin.readlines()]
    with open('source_ip_countries.txt', 'r') as fin:
        src_countries = [l.strip('\n') for l in fin.readlines()]

    dict_colors = discrete.__get_dict_colors(set(dest_countries + src_countries), colors=set_colors.set_colors[7])
    save_discr_pict(dest_countries, pict_path + 'dest_countries', curve_mode='hilbert',
                    max_len=4 ** 7, dict_colors=dict_colors)

    save_discr_pict(src_countries, pict_path + 'src_countries', curve_mode='hilbert',
                    max_len=4 ** 7, dict_colors=dict_colors)

    pass


def get_packets_sent():
    packets = [int(p) for p in spam_data['packets_sent']]
    # save_cont_pict(packets, path=pict_path + 'packets', curve_mode='hilbert',
    #                num_of_steps=10, max_len=4 ** 7,
    #                dict_colors=set_colors.set_colors[15])

    dur_pict, dur_legend = continuous.get_picture(data=packets,
                                                  curve_mode='hilbert',
                                                  max_len=4 ** 7,
                                                  num_of_steps=15,
                                                  colors=set_colors.set_colors[3])
    dur_pict.resize((700, 700)).save(pict_path + 'packets.png')
    dur_legend.save(pict_path + 'packets_legend.png')

    pass


if __name__ == '__main__':
    init()
    # get_hours_picture()
    # get_duration_pict()
    # get_ports_pict()
    # get_tcp_flags_pict()

    # get_ips_country()

    get_packets_sent()
    pass
