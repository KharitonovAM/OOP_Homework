import logging
from abc import ABC, abstractmethod
from typing import Any

from setting.log_setting import my_log_config

logging.basicConfig = my_log_config
# определяем именные логеры
logging_product = logging.getLogger("class_Product")


class BaseProduct(ABC):
    """Абстрактный класс - основа для создания продуктов"""

    @abstractmethod
    def __str__(self) -> None:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> None:
        pass

    @abstractmethod
    def new_product(self) -> None:
        pass

    @abstractmethod
    def price(self) -> None:
        pass


class MixinStartInfo:
    """Класс миксин, который ывводит на экран информацию об объекте"""

    def __init__(self):
        super().__init__()
        self.__repr__()

    def __repr__(self):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")


class Product(BaseProduct, MixinStartInfo):
    """Класс по созданию объектов Продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта класса Product"""

        logging_product.info("Начало инициации объекта класса Category")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        logging_product.info(
            f"Завершили инициацию объекта класса Category с параметрами name - {name}, "
            f"description - {description}, price - {price}, quantity-{quantity}"
        )

    def __str__(self) -> str:
        """Определяем правило для отображения печати объекта"""
        logging_product.info(
            f"вызвали на печать объект класса Product {self.name}, {self.__price} руб. Остаток: {self.quantity}"
        )

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        """Магический метод по сложению количества товара на складе"""

        logging_product.info("Вызвана попвтка сложить два объекта класса Product ")

        if isinstance(other, type(self)):
            comman_price = self.quantity * self.__price + other.quantity * other.__price
            logging_product.info(f"Сложение прошло нормально резульатат {comman_price}")
            return comman_price

        else:
            logging_product.error(f"Попытка сложения завершилась ошибкой втрой объект {other.__class__.__name__}")
            print(f"Оба объекта должны быть класса {(self.__class__.__name__)}")
            raise TypeError(f"Оба объекта должны быть класса {(self.__class__.__name__)}")

    @classmethod
    def new_product(cls, insert_dict: dict[Any, Any], insert_list: list = []):
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
        logging_product.info(f"Поступил запрос по получению данных цены у {self.name}")
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новое значение цены"""

        logging_product.info(
            f"Начинаем устанавливать новую цену {new_price} для {self.name}, предыдущая цена {self.__price}"
        )
        if self.__price > new_price:
            user_choise = ""
            while user_choise.lower() not in ("y", "n"):
                logging_product.info("Выполняем запрос пользователю на снижение цены")
                user_choise = input(
                    "\nНовая цена ниже чем предыдущая. Для подтверждение ввода сделайте выбор: "
                    "y - устанавливаем более нихку цену, n - сохранем предыдущую.\n"
                )
                logging_product.info(f"Получен ответ пользователя {user_choise}")
                if user_choise.lower() == "y":
                    logging_product.info("Пользователь утвердил снижение цены")
                    self.__price = new_price
                    if new_price <= 0:
                        logging_product.info("Уведомили пользователя об отрицательной цене")
                        print("Цена не должна быть нулевая или отрицательная")
        else:
            logging_product.info("Изменили на новую стоимость (как увеличение)")
            self.__price = new_price


class Smartphone(Product):
    """Класс по созданию объектов Смартфон, является дочерним от класса Продукт"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализация объекта класса Smartphone"""

        logging_product.info("Старт инициализации объекта смартфон")
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        logging_product.info("объект класса смартфон инициализирован полностью")


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация объекта класса LawnGrass"""

        logging_product.info("Старт инициализации объекта Трава Газонная")
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        logging_product.info("объект класса Трава Газонная инициализирован полностью")
