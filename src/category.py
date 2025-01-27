import logging
from abc import ABC, abstractmethod
from typing import Any

from setting.log_setting import my_log_config
from src.product import Product
from src.raises import ZeroQuantityError

logging.basicConfig = my_log_config
# определяем именные логеры
logging_category = logging.getLogger("class_Category")


class abstract_structure(ABC):
    """Абстрактный класс для создания классов для работы с продуктами"""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_product(self):
        pass


class Order(abstract_structure):

    def __init__(self, quantity, order_product):
        """инициализация объекта класса Order"""

        logging_category.info("Старт инициализации объекта категории Order")
        self.quantity = quantity
        if self.quantity ==0:
            raise ZeroQuantityError
        self.order_product = order_product
        self.total_account = quantity * order_product.price
        logging_category.info("Завершена инициализации объекта категории Order")

    def __str__(self):
        return (
            f"В заказе {self.order_product.name} в количестве {self.quantity} шт на общую сумму {self.total_account}"
        )

    def add_product(self, new_producr):
        """Добавляет новый продукт в заказ, заменяя текущий на новый"""

        logging_category.info("Пытаемся заменить продукт в заказе")
        try:
            if new_producr.quantity == 0:
                raise ZeroQuantityError
            else:
                self.order_product = new_producr
        except ZeroQuantityError as e:
            logging_category.error(f'При попытке добавить продукт возникла ошибка {e}')
            print(e)
        else:
            logging_category.info("Продукт в заказе заменён")
            print(f'{self.order_product.name} добавлен')
        finally:
            print('обработка добавления товара завершена')



    def recalculate_the_cost(self):
        """Метод который позволляет принудительно пересчитать общую стоимость заказа"""

        logging_category.info(f"Вызван метод по замене текущей суммы счета {self.total_account} на новую")
        self.total_account = self.quantity * self.order_product.price
        logging_category.info(f"Новая сумма счета {self.total_account}")


class Category(abstract_structure):
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
            f"Завершили инициацию объекта класса Category с параметрами name - " f"{name}, description - {description}"
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

    def get_avg_price(self) -> float:
        '''Метод который возвращает зачение средний цены для всех товаров в категории'''

        try:
            avg_price = sum([x.price for x in self.__products])/len(self.__products)
        except ZeroDivisionError:
            avg_price = 0.0
        return avg_price
