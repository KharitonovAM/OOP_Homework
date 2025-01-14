import logging
from typing import Any

from setting.log_setting import my_log_config

logging.basicConfig = my_log_config
# определяем именные логеры
logging_product = logging.getLogger("class_Product")


class Product:
    """Класс по созданию объектов Продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта класса Product"""

        logging_product.info("Начало инициации объекта класса Category")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        logging_product.info(
            f"Завершили инициацию объекта класса Category с параметрами name - {name}, "
            f"description - {description}, price - {price}, quantity-{quantity}"
        )

    @classmethod
    def new_product(cls, insert_dict: dict[Any, Any], insert_list=[]) -> None:
        '''принимает на вход параметры товара в словаре и возвращать созданный объект класса Product
        так же может принимать на вход список объектов Продукт и если находит совпадение, то
        возвращает максимальную цену и сумму количества объектов в образованном объекте'''

        logging_product.info("Начало инициации объекта класса Category c classmetod new_product")
        creating_product = cls(**insert_dict)
        logging_product.info(f"Создали новый объект на основе {insert_dict}")
        for item in insert_list:
            if item.name == creating_product.name:
                logging_product.info(f"Нашли совпедение с объектом из словаря у которого наименвоание {item.name}")
                creating_product.price = max(creating_product.price, item.price)
                creating_product.quantity += item.quantity
                logging_product.info(
                    f"Видоизменили объект и теперь цена {creating_product.price} и количество {creating_product.quantity}")
        return creating_product
