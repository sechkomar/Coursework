import pandas as pd

import set_colors

import discrete
import continuous

folder_path = "/media/sechko/D814F3AB14F38AB0/coursework/VizSec/spam/"
filename = 'spam.csv'
pict_path = 'pictures/'
spam_data = pd.read_csv(folder_path + filename)

columns = ['time', 'duration', 'source_ip', 'dest_ip', 'source_port', 'dest_port',
           'protocol', 'tsp_flags', 'tos', 'smth', 'packets_sent', 'bytes_sent', 'verdict']


def get_hours_picture():
    hours = [time.hour for time in spam_data.time]
    hours_pict, colors = discrete.get_picture(data=hours, curve_mode='hilbert', max_len=4 ** 7,
                                              colors=set_colors.set_colors[0])
    hours_pict.resize((700, 700)).save('pictures/hours.png')
    colors.save('pictures/hours_legend.png')


def init():
    spam_data.columns = columns
    print spam_data.head()
    spam_data.time = pd.to_datetime(spam_data.time)
    pass


def get_duration_pict():
    durations = spam_data['duration']
    dur_pict, dur_legend = continuous.get_picture(data=durations,
                                                  curve_mode='hilbert',
                                                  max_len=4 ** 7,
                                                  num_of_steps=50,
                                                  colors=set_colors.set_colors[5])
    dur_pict.resize((700, 700)).save(pict_path + 'durations.png')
    dur_legend.save(pict_path + 'durations_legend.png')


def get_source_ports_pict():
    source_ports = spam_data['source_port']
    scr_ports_pict, scr_ports_leg = continuous.get_picture(data=source_ports,
                                                           curve_mode='hilbert',
                                                           num_of_steps=10,
                                                           max_len=4 ** 7,
                                                           colors=set_colors.set_colors[0])

    scr_ports_pict.resize((700, 700)).save(pict_path + 'src_ports.png')
    scr_ports_leg.save(pict_path + 'src_ports_leg.png')


def get_tcp_flags_pict():
    flags = spam_data['tsp_flags']
    flags_pict, flags_leg = discrete.get_picture(data=flags, curve_mode='hilbert', max_len=4 ** 7,
                                              colors=set_colors.set_colors[8])
    flags_pict.resize((700, 700)).save('pictures/flags.png')
    flags_leg.save('pictures/flags_legend.png')



if __name__ == '__main__':
    init()
    get_hours_picture()
    # get_duration_pict()
    # get_source_ports_pict()
    # get_tcp_flags_pict()