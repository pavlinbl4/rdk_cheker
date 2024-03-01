import re
import os
from check_article_status import check_article_status
from check_existing_file import create_dir
from driver_job import get_spans, get_work_map
from pickle_files import load_pickle, dump_pickle, delete_old_pickle
from time_zone import get_city_time
from loguru import logger

logs_dir = create_dir('Logs')
custom_formatter = "<red>{time:YYYY-MM-DD HH:mm}</red> | <level>{level}</level> | <cyan>{message}</cyan>"
logger.add(f'{logs_dir}/debug.log', format=custom_formatter)


def find_article_status(article_status='GetImage.axd?kind=WF&key=E&site=RDK2SPB'):
    pattern = r'(?<=key=).*(?==RDK2SPB)'
    return re.findall(pattern, article_status)[0]


def get_article_status():
    # create today day string look like '28-02-2024'
    today_filename = get_city_time('Europe/Moscow').strftime("%d-%m-%Y")

    pickle_folder = 'Pickle_files'
    path_to_pickle_folder = create_dir(pickle_folder)  # create folder for pickle files
    delete_old_pickle(today_filename, path_to_pickle_folder)

    article_dict = {}

    if os.path.exists(f'{path_to_pickle_folder}/{today_filename}.pickle'):
        logger.info(f"file {today_filename}.pickle exist")
        article_dict = load_pickle(path_to_pickle_folder, today_filename)
    else:
        logger.info(f"No {today_filename}.pickle now")

    work_map = get_work_map()

    logger.info(f"in RDK now -  {len(work_map) - 1} notes")
    for x in range(1, len(work_map)):
        all_trs = work_map[x].find_elements('xpath', 'td')
        article_name = all_trs[0].text
        article_status = find_article_status(all_trs[5].find_element('xpath', 'img').get_attribute('src'))
        logger.info(f'Note {x} : {article_name} -- {article_status}')

        # if len(article_name) > 0 and article_name not in article_dict:
        if article_name not in article_dict:
            logger.info(f'added to dict : {article_name} -- {article_status}')

            article_dict[article_name] = article_status

            dump_pickle(pickle_folder, today_filename, article_dict)
            logger.info("Pickle file updated")

        else:
            logger.info(f"No new articles in RDK now")
        check_article_status(article_name, article_status, today_filename, path_to_pickle_folder)


if __name__ == '__main__':
    get_article_status()
