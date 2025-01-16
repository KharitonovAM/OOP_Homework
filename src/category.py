import logging
from typing import Any

from setting.log_setting import my_log_config
from src.product import Product

logging.basicConfig = my_log_config
# определяем именные логеры
logging_category = logging.getLogger("class_Category")


class Category:
    """Класс по созданию объектов Category"""

    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Any]) -> None:
        """Инициализация объекта класса Category"""

        logging_category.info("Начало инициации объекта класса Category")
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1
        logging_category.info(
            f"Завершили инициацию объекта класса Category с параметрами name - "
            f"{name}, description - {description}, products - {products}"
        )

    def add_product(self, new_product: Product) -> None:
        """Добавляет новый объект класса Product в список продуктов"""

        logging_category.info(f"Начиинаем добавлять в список продуктов {new_product.name}")
        Category.product_count += 1
        logging_category.info(f"Продукт с наименованием {new_product.name} успешно обавлен в список к {self.name}")
        self.__products.append(new_product)

    @property
    def products(self) -> None:
        """Геттер, выводящий информацию о продуктах, находящихся в категории"""

        logging_category.info("Выводим на экран информацию о продуктах")
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
            logging_category.info(
                f"Вывели на экран: {product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
