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
    def new_product(cls, insert_dict: dict[Any, Any]):
        '''принимает на вход параметры товара в словаре и возвращать созданный объект класса Product'''

        return cls(**insert_dict)