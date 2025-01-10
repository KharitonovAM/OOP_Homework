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
                         ['Iphone 15', 'Iphone 14', 'Iphone 13'],
                    )


@pytest.fixture
def tv_category():
    return Category("Телевизоры",
                         "Телевизор это не только передача информации, но и зомбирование населения",
                         ['Wollmer QLED HL55 Onyx', 'Яндекс ТВ Станция Pro YaGPT 55', 'TCL 55C655 Pro', 'Hisense 55U6KQ', 'Xiaomi TV A Pro 55'],
                    )