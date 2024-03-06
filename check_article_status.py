from check_existing_file import create_dir
from pickle_files import load_pickle, dump_pickle
from send_message_to_telegram import send_telegram_message
from loguru import logger
from telegram_dict import add_telegram_message
from icecream import ic


# logs_dir = create_dir('Logs')
# custom_formatter = "<red>{time:YYYY-MM-DD HH:mm}</red> | <level>{level}</level> | <cyan>{message}</cyan>"
# logger.add(f'{logs_dir}/debug.log', format=custom_formatter)
# logger.add(f'{logs_dir}/debug.log')


def check_article_status(today_filename, path_to_pickle_folder, article_dict):
    # article_dict = load_pickle(path_to_pickle_folder, today_filename)
    article_dict.setdefault('telegram_info', [])

    for article_name, article_status in article_dict.items():
        print(article_name, article_status)
        try:
            if article_status == '***&site':
                if article_name not in article_dict['telegram_info']:
                    logger.info(f'New message was sent \n{article_name} - {article_status}')
                    send_telegram_message(f'{article_name} - {article_status}')
                    article_dict = add_telegram_message(article_dict, article_name)
                    article_dict[article_name] = article_status
                    # dump_pickle(path_to_pickle_folder, today_filename, article_dict)
                else:
                    logger.info(f'The message was sent earlier {article_name} - {article_status}')

            # else:
            #     logger.info("No changes in pickle file")
        except KeyError as key:
            send_telegram_message(f'No such line in RDK - {key}')
            logger.error(f'No such line in RDK - {key}')
        dump_pickle(path_to_pickle_folder, today_filename, article_dict)

if __name__ == '__main__':
    check_article_status('04-03-2024', "Pickle_files")
