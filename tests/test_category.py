import pytest

def test_make_object_category(phone_category):
    '''Тестируем, что функционал по созданию объекта класса Category работает корректно'''

    test_category = phone_category
    assert test_category.name == "Смартфоны"
    assert test_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert test_category.products == ['Iphone 15', 'Iphone 14', 'Iphone 13']


def test_count_number_of_categories(phone_category, tv_category):
    '''Функция по тестированию функционала подсчета количеста наименований товара, принимает на вход 2 фикстуры
    проверяет что количество наименований подсчитано вверно и доступно из любой категории'''
    test_category1 = phone_category
    test_category2 = tv_category
    assert test_category1.count_names == 8
    assert test_category2.count_names == 8


def test_counting_number_of_categories(phone_category, tv_category):
    '''Функция по тестированию функционала подсчета количеста созданных категорий, принимает на вход 2 фикстуры
        проверяет что подсчет количества созданных категорий осуществляется верно и доступно из любой категории'''
    test_category1 = phone_category
    test_category2 = tv_category
    assert test_category1.count_category == 2
    assert test_category2.count_category == 2
