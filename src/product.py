import logging
from typing import Any

from setting.log_setting import my_log_config

logging.basicConfig = my_log_config
# определяем именные логеры
logging_product = logging.getLogger("class_Product")


class Product:
    """Класс по созданию объектов Продукт"""


    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта класса Product"""

        logging_product.info("Начало инициации объекта класса Category")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        logging_product.info(
            f"Завершили инициацию объекта класса Category с параметрами name - {name}, "
            f"description - {description}, price - {price}, quantity-{quantity}"
        )


    @classmethod
    def new_product(cls, insert_dict: dict[Any, Any], insert_list:list = []) -> Product:
        """принимает на вход параметры товара в словаре и возвращать созданный объект класса Product
        так же может принимать на вход список объектов Продукт и если находит совпадение, то
        возвращает максимальную цену и сумму количества объектов в образованном объекте"""

        logging_product.info("Начало инициации объекта класса Category c classmetod new_product")
        creating_product = cls(**insert_dict)
        logging_product.info(f"Создали новый объект на основе {insert_dict}")
        for item in insert_list:
            if item.name == creating_product.name:
                logging_product.info(f"Нашли совпедение с объектом из словаря у которого наименвоание {item.name}")
                creating_product.__price = max(creating_product.__price, item.__price)
                creating_product.quantity += item.quantity
                logging_product.info(
                    f"Видоизменили объект и теперь цена {creating_product.__price} и количество "
                    f"{creating_product.quantity}"
                )
        return creating_product


    @property
    def price(self) -> float:
        """Геттер для получения данных о значении параметра цена"""

        return self.__price


    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новое значение цены"""

        if self.__price > new_price:
            user_choise = ""
            while user_choise.lower() not in ("y", "n"):
                user_choise = input(
                    "\nНовая цена ниже чем предыдущая. Для подтверждение ввода сделайте выбор: "
                    "y - устанавливаем более нихку цену, n - сохранем предыдущую.\n"
                )
                if user_choise.lower() == "y":
                    self.__price = new_price
                    if new_price <= 0:
                        print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
