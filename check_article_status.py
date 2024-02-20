import pickle
from send_message_to_telegram import send_telegram_message
from pathlib import Path
from icecream import ic


def check_article_status(article_name, article_status, today_filename):
    with open(f'{Path.home()}/{today_filename}.pickle', 'rb') as articles:
        article_dict = pickle.load(articles)
        # ic(article_dict)

    if article_dict[article_name] != article_status and article_status == '***&site':
        send_telegram_message(article_name)
        print(f'old status of {article_name} - {article_status}')
        article_dict[article_name] = article_status
        print(f'new status of {article_name} - {article_status}')

        with open(f'{Path.home()}/{today_filename}.pickle', 'wb') as f:
            pickle.dump(article_dict, f)
    else:
        print("No changes in pickle file")


if __name__ == '__main__':
    check_article_status('фарватер на утро', '***&site', '20_02_24')
