import json
import os

from src.init import make_object_from_dict, take_data_from_json


def test_take_data_from_json(my_dict):
    """Создаем файл, записывем в него данные из словаря (фикстуры),
    получаем из него данные при помощи функции take_data_from_json.
     временный файл удалем и проверем корректность полученной информации"""
    my_data_dict = my_dict
    with open("temp_file.txt", "w", encoding="utf-8") as file:
        json.dump(my_data_dict, file)
    try:
        data_from_file = take_data_from_json("temp_file.txt")
    finally:
        os.remove("temp_file.txt")
    assert data_from_file == my_data_dict


def test_make_object_from_dict(dict_for_json):
    test_object_list = make_object_from_dict(dict_for_json)
    print(test_object_list)
    assert test_object_list[0].name == "Смартфоны"
    assert (
        test_object_list[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
