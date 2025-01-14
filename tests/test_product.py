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
    assert Product(product_dict1) == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_new_product1(product_dict2):
    '''Проверяет функционал метода new_product, принимающий словарь и возвращающь экземпляр класса Product'''
    assert Product(product_dict1) == Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)