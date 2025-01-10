import pytest

import src.category


def test_make_object_category(phone_category):
    """Тестируем, что функционал по созданию объекта класса Category работает корректно"""

    test_category = phone_category
    assert test_category.name == "Смартфоны"
    assert (
        test_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_category.products == ["Iphone 15", "Iphone 14", "Iphone 13"]


def test_count_number_of_categories(clear_cash, phone_category, tv_category):
    """Функция по тестированию функционала подсчета количеста наименований товара, принимает на вход 2 фикстуры
    проверяет что количество наименований подсчитано вверно и доступно из любой категории"""

    clear_cash
    test_category1 = phone_category
    test_category2 = tv_category
    assert test_category1.product_count == 8
    assert test_category2.product_count == 8


def test_counting_number_of_categories(clear_cash, phone_category, tv_category):
    """Функция по тестированию функционала подсчета количеста созданных категорий, принимает на вход 2 фикстуры
    проверяет что подсчет количества созданных категорий осуществляется верно и доступно из любой категории"""

    clear_cash
    test_category1 = phone_category
    test_category2 = tv_category
    assert test_category1.category_count == 2
    assert test_category2.category_count == 2


def test_not_enough_variables():
    """Тестирование возникновения ошибки в случае передачи недостаточного количества аргументов"""
    with pytest.raises(TypeError):
        src.category.Category("somename", "somedescription")
