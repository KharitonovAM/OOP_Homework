import pytest

from src.product import Product


def test_making_object_Product(my_phone : Product) -> None:
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


def test_new_product1(product_dict1):
    '''Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product'''
    assert Product.new_product(product_dict1).name == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).name
    assert Product.new_product(product_dict1).description == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).description
    assert Product.new_product(product_dict1).price == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).price
    assert Product.new_product(product_dict1).quantity == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14).quantity


def test_new_product1(product_dict2):
    '''Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product'''
    assert Product.new_product(product_dict2).name == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).name
    assert Product.new_product(product_dict2).description == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).description
    assert Product.new_product(product_dict2).price == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).price
    assert Product.new_product(product_dict2).quantity == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7).quantity