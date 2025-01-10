import json
from typing import Any, ClassVar

import setting.setting
from src.category import Category
from src.product import Product


def take_data_from_json(filename: str) -> dict[Any:Any]:
    '''Принимает на вход путь к json файлу, возвращает словать с информцей из json-файла '''

    with open(filename, 'r', encoding='utf-8') as file:
        data_from_file = json.load(file)
    return data_from_file


def make_object_from_dict(inncomming_data: dict[Any:Any]) -> list[ClassVar]:
    '''Принимает словарь и возвращает список объектов классов'''

    list_category = []
    for category_data in inncomming_data:
        list_products = []
        for product_data in category_data['products']:
            product = Product(**product_data)
            list_products.append(product)
        category = Category(name=category_data['name'], description=category_data['description'], products=list_products)
        list_category.append(category)
    return list_category


# if __name__ == '__main__':
#     z = take_data_from_json(setting.setting.json_file)
#     print(z)
#     l = make_object_from_dict(z)
#     print(l[0].products[0].name)

