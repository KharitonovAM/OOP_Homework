import logging

from setting.setting import my_log_config

# импортируем настройки логирования
logging.basicConfig = my_log_config

# определяем именные логеры
logging_product = logging.getLogger("class_Product")


class Product:
    """Класс по созданию объектов Продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
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
