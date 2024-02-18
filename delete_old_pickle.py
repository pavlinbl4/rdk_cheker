import glob
import os
from pathlib import Path
import re

def file_name(pickle_file):
    return re.findall(r'\d{2}_\d{2}_\d{2}', pickle_file)[0]

def delete_old_pickle(today_filename):
    if len(glob.glob(f'{Path.home()}/*.pickle')) != 0:
        pickle_file = glob.glob(f'{Path.home()}/*.pickle')[0]
        # print(file_name(pickle_file))
        if file_name(pickle_file) != today_filename:
            os.remove(pickle_file)
        # print("fresh file")


if __name__ == '__main__':
    delete_old_pickle("18_02_24.pickle")
    # print(file_name('/Users/evgeniy/18_02_24.pickle'))
