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
