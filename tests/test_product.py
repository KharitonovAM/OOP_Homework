import pytest
from typing import Any

from src.product import Product


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
    '''Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product'''
    assert Product.new_product(product_dict1).name == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).name
    assert Product.new_product(product_dict1).description == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0,
                                                                     14).description
    assert Product.new_product(product_dict1).price == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0,
                                                               14).price
    assert Product.new_product(product_dict1).quantity == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0,
                                                                  14).quantity


def test_new_product2(product_dict2: dict[str, Any]) -> None:
    '''Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product'''

    assert Product.new_product(product_dict2).name == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).name
    assert Product.new_product(product_dict2).description == Product('55" QLED 4K', "Фоновая подсветка", 123000.0,
                                                                     7).description
    assert Product.new_product(product_dict2).price == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).price
    assert Product.new_product(product_dict2).quantity == Product('55" QLED 4K', "Фоновая подсветка", 123000.0,
                                                                  7).quantity


def test_new_product_upgrade(my_phone: Product):
    '''Тестирует расширенный функционал new_product с проверкой наличия добавляемого продукта уже в списке продуктов'''

    my_list = [my_phone]
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert Product.new_product(
        {'name': 'Iphone 15', 'description': "512GB, Gray space", 'price': 15000, 'quantity': 12},
        my_list).price == 210000.0
    assert Product.new_product(
        {'name': 'Iphone 15', 'description': "512GB, Gray space", 'price': 15000, 'quantity': 12},
        my_list).quantity == 20


def test_new_price():
    my_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    my_product.price = 1500000
    assert my_product.price == 1500000