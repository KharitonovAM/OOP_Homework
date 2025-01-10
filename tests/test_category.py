import pytest

def test_make_object_category(phone_category):
    '''Тестируем, что функционал по созданию объекта класса Category работает корректно'''

    test_category = phone_category
    assert test_category.name == "Смартфоны"
    assert test_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    assert test_category.description == ['Iphone 15', 'Iphone 14', 'Iphone 13']