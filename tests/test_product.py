import pytest

import src.product


def test_making_object_Product(my_phone):
    """Тестируем, что функционал по созданию объекта класса Product работает корректно:"""
    my_phone_object = my_phone
    assert my_phone_object.name == "Iphone 15"
    assert my_phone_object.description == "512GB, Gray space"
    assert my_phone_object.price == 210000.0
    assert my_phone_object.quantity == 8


def test_not_enough_variables():
    """Тестирование возникновения ошибки в случае передачи недостаточного количества аргументов"""
    with pytest.raises(TypeError):
        src.product.Product("somename", "somedescription")
