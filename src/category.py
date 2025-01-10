import logging

from setting.setting import my_log_config

# импортируем настройки логирования
logging.basicConfig = my_log_config

# определяем именные логеры
logging_category = logging.getLogger("class_Category")


class Category:
    """Класс по созданию объектов Category"""

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products) -> None:
        """Инициализация объекта класса Category"""

        logging_category.info("Начало инициации объекта класса Category")
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1
        logging_category.info(
            f"Завершили инициацию объекта класса Category с параметрами name - "
            f"{name}, description - {description}, products - {products}"
        )
