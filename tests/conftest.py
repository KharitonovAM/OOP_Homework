import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def my_phone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture
def phone_category():
    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         ['Iphone 15', 'Iphone 14', 'Iphone 13'])