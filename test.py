import pandas as pd
import discrete
from colour import Color

def main():
    path = '/home/sechko/z_Coursework/attack set/blacklist_march_week3_csv/march/week3/blacklist_flows_cut.csv'
    data = pd.read_csv(path, header=None, nrows=20000 + 32 ** 2)
    data = data[20000:]
    first_ips = [int((ip.split('.'))[0]) for ip in data[3]]

    # ips_image = discrete.get_horizontal_line_pict(data=first_ips, size=(32, 32))
    # ips_image.resize((500, 500)).save('first_ips.png')

    # ips_hilbert = discrete.get_hilbert_pict(data=first_ips, max_len=32 ** 2)
    # ips_hilbert.resize((500, 500)).save('first_ips_hilbert_1.png')

    ips_hilbert = discrete.get_picture(data=first_ips, curve_mode='hilbert', max_len=32 ** 2)
    ips_hilbert.resize((500, 500)).save('first_ips_hilbert_1.png')






if __name__ == '__main__':
    main()