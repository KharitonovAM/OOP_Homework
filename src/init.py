import json


def take_data_from_json(filename):
    '''Принимает на вход путь к json файлу, возвращает словать с информцей из json-файла '''

    with open(filename, 'r', encoding='utf-8') as file:
        data_from_file = json.load(file)
    return data_from_file