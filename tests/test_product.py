from typing import Any
from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone


def test_making_object_Product(my_phone: Product) -> None:
    """Тестируем, что функционал по созданию объекта класса Product работает корректно:"""

    my_phone_object = my_phone
    assert my_phone_object.name == "Iphone 15"
    assert my_phone_object.description == "512GB, Gray space"
    assert my_phone_object.price == 210000.0
    assert my_phone_object.quantity == 8


def test_not_enough_variables() -> None:
    """Тестирование возникновения ошибки в случае передачи недостаточного количества аргументов"""

    with pytest.raises(TypeError):
        Product("somename", "somedescription")


def test_new_product1(product_dict1: dict[str, Any]) -> None:
    """Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product"""
    assert (
        Product.new_product(product_dict1).name == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).name
    )
    assert (
        Product.new_product(product_dict1).description
        == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).description
    )
    assert (
        Product.new_product(product_dict1).price == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).price
    )
    assert (
        Product.new_product(product_dict1).quantity
        == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).quantity
    )


def test_new_product2(product_dict2: dict[str, Any]) -> None:
    """Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product"""

    assert Product.new_product(product_dict2).name == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).name
    assert (
        Product.new_product(product_dict2).description
        == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).description
    )
    assert Product.new_product(product_dict2).price == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).price
    assert (
        Product.new_product(product_dict2).quantity
        == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).quantity
    )


def test_new_product_upgrade(my_phone: Product) -> None:
    """Тестирует расширенный функционал new_product с проверкой наличия добавляемого продукта уже в списке продуктов"""

    my_list = [my_phone]
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert (
        Product.new_product(
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 15000, "quantity": 12}, my_list
        ).price
        == 210000.0
    )
    assert (
        Product.new_product(
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 15000, "quantity": 12}, my_list
        ).quantity
        == 20
    )


def test_new_price() -> None:
    """Тестируем функцию установление новой стоимости"""
    my_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    my_product.price = 15000000
    assert my_product.price == 15000000


@patch("src.product.input", side_effect=["y"])
def test_new_price_low_0(capsys: pytest.CaptureFixture) -> None:
    """Проверяем корректность поведения при попытке установить стоимость ниже 0"""
    my_phone = Product("product_name", "product_decription", 200000, 5)
    my_phone.price = -1500000
    my_priner = capsys.readouterr()
    assert my_priner


@patch("src.product.input", side_effect=["g", "n"])
def test_new_price_chang_low(input, my_phone):
    """Тест проверяет случай когда пользователь несогласен изменять стоимость на болюю низкую"""

    my_phone.price = 1500
    assert my_phone.price == 210000.0


@patch("src.product.input", side_effect=["k", "y"])
def test_new_price_chang_low2(input, my_phone: Product) -> None:
    """Тест проверяет случай когда пользователь согласен изменять стоимость на болюю низкую"""

    z = my_phone
    z.price = 1500
    assert z.price == 1500


def test_magic_str_by_product(my_phone: Product, capsys: pytest.CaptureFixture) -> None:
    """Проверяем функционал, что при вызове на печать объекта класса Product получаем результат
    который требуется в соответствии с ТЗ"""

    print(my_phone)
    test_printer = capsys.readouterr()
    assert test_printer.out == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_add_by_product(my_phone: Product) -> None:
    """Проверяем, что если сложить два объекта из класса Product
    получим в результате сумму товаров на складе"""

    test_other = Product("test_name", "test_descripion", 150000, 15)
    assert my_phone + test_other == 8 * 210000 + 150000 * 15


def test_creation_smartfone(smartfon_product: Smartphone) -> None:
    """Тест проверяет что создаётся объект класса Cmartfone и что атрибуты соответствуют ожиданиям
    для тестирования применяется фикстура smartfon_product"""

    assert smartfon_product.name == "Iphone 15"
    assert smartfon_product.description == "512GB, Gray space"
    assert smartfon_product.price == 210000.0
    assert smartfon_product.quantity == 8
    assert smartfon_product.efficiency == 98.2
    assert smartfon_product.model == "15"
    assert smartfon_product.memory == 512
    assert smartfon_product.color == "Gray space"


def test_creation_lawngrass(lawngrass_product: LawnGrass) -> None:
    """Тест проверяет. что созданный объект класса LawnGrass соответствует ТЗ"""

    assert lawngrass_product.name == "Газонная трава"
    assert lawngrass_product.description == "Элитная трава для газона"
    assert lawngrass_product.price == 500.0
    assert lawngrass_product.quantity == 20
    assert lawngrass_product.country == "Россия"
    assert lawngrass_product.germination_period == "7 дней"
    assert lawngrass_product.color == "Зеленый"


def test_add_product_diff_classes(lawngrass_product, smartfon_product):
    with pytest.raises(TypeError):
        lawngrass_product + smartfon_product
