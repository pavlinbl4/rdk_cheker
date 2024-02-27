import pickle
from icecream import ic


def load_pickle(pickle_folder, pickle_file_name):
    with open(f'{pickle_folder}/{pickle_file_name}.pickle', 'rb') as articles:
        article_dict = pickle.load(articles)
    return article_dict


def dump_pickle(pickle_folder, pickle_file_name, article_dict):
    with open(f'{pickle_folder}/{pickle_file_name}.pickle', 'wb') as f:
        pickle.dump(article_dict, f)


if __name__ == '__main__':
    ic(load_pickle('Pickle_files', '27-02-2024'))
    e_dict = {'СКА СТАВИМ СРАЗУ': 'W&site',
                 'невкосметика ставить немедля': 'W&site',
                 'парнас ставить сразу ж': 'W&site',
                 'рынок рекламы на утро': 'E&site',
                 'театрал срочно в номер': 'W&site',
                 'шевченко ставить тотчас': 'W&site'}
    # dump_pickle('Pickle_files', '27-02-2024',e_dict)
