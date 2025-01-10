import pytest


def test_making_object_Product(my_phone):
    '''Тестируем, что функционал по созданию объекта класса Product работает корректно:'''
    my_phone_object = my_phone
    assert my_phone_object.name == "Iphone 15"
    assert my_phone_object.description == "512GB, Gray space"
    assert my_phone_object.price == 210000.0
    assert my_phone_object.quantity == 8
