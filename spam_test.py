import pandas as pd

import set_colors

import discrete
import continuous

folder_path = "/media/sechko/D814F3AB14F38AB0/coursework/VizSec/spam/"
filename = 'spam.csv'
pict_path = 'pictures/'
spam_data = pd.read_csv(folder_path + filename)


def get_hours_picture():
    hours = [time.hour for time in spam_data.time]
    hours_pict, colors = discrete.get_picture(data=hours, curve_mode='hilbert', max_len=4 ** 7,
                                              colors=set_colors.set_colors[0])
    hours_pict.resize((700, 700)).save('pictures/hours.png')
    colors.save('pictures/hours_legend.png')


def init():
    spam_data.time = pd.to_datetime(spam_data.time)
    pass


def get_duration_pict():
    durations = spam_data['duration']
    dur_pict, dur_legend = continuous.get_picture(durations, curve_mode='hilbert', max_len= 4 ** 7, num_of_steps=12,
                           colors=set_colors.set_colors[0])
    dur_pict.resize((700, 700)).save(pict_path + 'durations.png')
    dur_legend.save(pict_path + 'durations_legend.png')

if __name__ == '__main__':
    init()
    # get_hours_picture()
    get_duration_pict()
