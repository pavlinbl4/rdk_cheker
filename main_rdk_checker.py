
from check_article_status import check_article_status
from check_existing_file import create_dir
from driver_job import get_work_map
from pickle_files import load_pickle, dump_pickle, delete_old_pickle
from time_zone import get_city_time
from loguru import logger

logs_dir = create_dir('Logs')
# logs_dir = 'Logs'
# custom_formatter = "<red>{time:YYYY-MM-DD HH:mm}</red> | <level>{level}</level> | <cyan>{message}</cyan>"
# logger.add(f'{logs_dir}/debug.log', format=custom_formatter)
logger.add(f'{logs_dir}/debug.log')


def get_article_status():
    # create today day string look like '28-02-2024'
    today_filename = get_city_time('Europe/Moscow').strftime("%d-%m-%Y")

    # create dict for articles
    article_dict = {}

    # set folder to pickle files
    pickle_folder = 'Pickle_files'
    path_to_pickle_folder = create_dir(pickle_folder)  # create folder for pickle files
    # logger.info(f"{path_to_pickle_folder}")

    # delete old pickle file
    delete_old_pickle(today_filename, path_to_pickle_folder)

    # create new pickle file
    dump_pickle(path_to_pickle_folder, today_filename, article_dict)

    # # if picle file exist load info from pickle to article_dict
    # if os.path.exists(f'{path_to_pickle_folder}/{today_filename}.pickle'):
    #     logger.info(f"file {today_filename}.pickle exist")
    #     article_dict = load_pickle(path_to_pickle_folder, today_filename)
    # else:
    #     logger.info(f"No {today_filename}.pickle now")

    # get information from RDK site
    fresh_article_dict = get_work_map()

    if article_dict != fresh_article_dict:
        article_dict.update(fresh_article_dict)

        dump_pickle(path_to_pickle_folder, today_filename, article_dict)

        logger.info("Pickle file updated")
    else:
        logger.info(f"No new articles in RDK now")

    check_article_status(today_filename, path_to_pickle_folder)


if __name__ == '__main__':
    get_article_status()
