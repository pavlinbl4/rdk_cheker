# script to delete old files

import datetime
import os
from icecream import ic
from check_existing_file import create_dir

ic.disable()


# Configure logger to delete files older than 7 days
def delete_old_log_files(logs_dir):
    now = datetime.datetime.now()
    ic(now)
    ic(datetime.timedelta(days=1))
    ic((now - datetime.timedelta(days=1)).timestamp())
    ic(type(now - datetime.timedelta(days=1)))
    for log_filename in os.listdir(logs_dir):
        if log_filename.endswith(".log") and os.path.getmtime(f'{logs_dir}/debug.log') < (
                now - datetime.timedelta(days=1)).timestamp():
            os.remove(f'{logs_dir}/debug.log')
            print("File deleted")
    print('File is fresh')


# loguru.logger.add(sink=delete_old_log_files, level='DEBUG')
if __name__ == '__main__':
    logs_dir = create_dir('Logs')
    print(logs_dir)
    delete_old_log_files(logs_dir)
