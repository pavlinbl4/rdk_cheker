from pickle_files import load_pickle, dump_pickle
from send_message_to_telegram import send_telegram_message
import logging

logging.basicConfig(level=logging.INFO, filename='my_lol.log', datefmt='$Y/$m/$d  %I/%M', encoding='utf-8',
                    filemode='w+')


def check_article_status(article_name, article_status, today_filename, pickle_folder):
    article_dict = load_pickle(pickle_folder, today_filename)

    try:
        if article_dict[article_name] != article_status and article_status == '***&site':
            send_telegram_message(article_name)
            logging.info(f'old status of {article_name} - {article_status}')
            print(f'old status of {article_name} - {article_status}')
            article_dict[article_name] = article_status
            print(f'new status of {article_name} - {article_status}')

            dump_pickle(pickle_folder, today_filename, article_dict)
        else:
            print("No changes in pickle file")
    except KeyError as key:
        send_telegram_message(f'No such line in RDK - {key}')
        print(f'No such line in RDK - {key}')


if __name__ == '__main__':
    check_article_status('фарватер на утро', '***&site', '26-02-2024', 'Pickle_files')
