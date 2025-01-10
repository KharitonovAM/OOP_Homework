import json
import logging
from typing import Any, ClassVar

from setting.setting import my_log_config
from src.category import Category
from src.product import Product

# импортируем настройки логирования
logging.basicConfig = my_log_config
# определяем именные логеры
logging_init = logging.getLogger("modul init")


def take_data_from_json(filename: str) -> dict[Any, Any]:
    """Принимает на вход путь к json файлу, возвращает словать с информцей из json-файла"""

    logging_init.info(f"Старт извлечения данных из json файла {filename}")
    with open(filename, "r", encoding="utf-8") as file:
        data_from_file = json.load(file)
    logging_init.info(f"Данные из {filename} успешно получены")
    return data_from_file


def make_object_from_dict(inncomming_data: dict[Any, Any]) -> list[ClassVar]:
    """Принимает словарь и возвращает список объектов классов"""

    logging_init.info(f"Для формирования объектов получили словарь {inncomming_data}")
    list_category = []
    for category_data in inncomming_data:
        logging_init.info("Старт формирования объекта Категория")
        list_products = []
        for product_data in category_data["products"]:
            logging_init.info("Старт формирования объекта Продукт")
            product = Product(**product_data)
            list_products.append(product)
            logging_init.info("Объект класса Продукт сформирован")
        category = Category(
            name=category_data["name"], description=category_data["description"], products=list_products
        )
        list_category.append(category)
        logging_init.info("объект класса Категория сформирован")
    return list_category
