import json
from typing import Any, ClassVar


def take_data_from_json(filename: str) -> dict[Any:Any]:
    '''Принимает на вход путь к json файлу, возвращает словать с информцей из json-файла '''

    with open(filename, 'r', encoding='utf-8') as file:
        data_from_file = json.load(file)
    return data_from_file


def make_object_from_dict(inncomming_data: dict[Any:Any]) -> list[ClassVar]:
    '''Принимает словарь и возвращает список объектов классов'''
    pass
