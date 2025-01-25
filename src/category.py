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

    def __str__(self) -> str:
        """Волшебный метод. который возвращает
        Название категории, количество продуктов: сумма шт."""

        logging_category.info("вызвали на печать __str__ Product")
        total_count = 0
        for prod in self.__products:
            total_count += prod.quantity
        return f"{self.name}, количество продуктов: {total_count} шт."

    def add_product(self, new_product: Any) -> None:
        """Добавляет новый объект класса Product в список продуктов"""
        logging_category.info("Начиинаем добавлять в список продуктов")
        if issubclass(type(new_product), Product):
            Category.product_count += 1
            self.__products.append(new_product)
            logging_category.info(f"Продукт с наименованием {new_product.name} успешно обавлен в список к {self.name}")
        else:
            logging_category.error("Попытка добавить продукт с наименованием завершилась ошибкой")
            raise TypeError

    @property
    def products(self) -> None:
        """Геттер, выводящий информацию о продуктах, находящихся в категории"""

        data_about_products = ""
        logging_category.info("Выводим на экран информацию о продуктах")
        for i in range((len(self.__products))):
            data_about_products += f"{self.__products[i]}\n"
            logging_category.info(
                f"Вывели на экран: {self.__products[i].name}, "
                f"{self.__products[i].price} руб. Остаток: {self.__products[i].quantity} шт."
            )
        return data_about_products

    def product_list(self) -> list[Product]:
        """Функция которая позволяет получиь список продуктов"""
        return self.__products
