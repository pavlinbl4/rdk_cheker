import glob
import os
from pathlib import Path
import re

def file_name(pickle_file):
    return re.findall(r'\d{2}-\d{2}-\d{2}', pickle_file)[0]

def delete_old_pickle(today_filename,pickle_folder):
    if len(glob.glob(f'{pickle_folder}/*.pickle')) != 0:
        pickle_file = glob.glob(f'{pickle_folder}/*.pickle')[0]
        # print(file_name(pickle_file))
        if file_name(pickle_file) != today_filename:
            os.remove(pickle_file)
        # print("fresh file")


if __name__ == '__main__':
    delete_old_pickle("28_02_24.pickle", 'Piclkle_files')
    # print(file_name('/Users/evgeniy/18_02_24.pickle'))
