import pytest
from typing import Any

from src.category import Category
from src.product import Product


@pytest.fixture
def my_phone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def phone_category() -> Category:
    phone_category_object = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Iphone 15", "Iphone 14", "Iphone 13"],
    )
    return phone_category_object


@pytest.fixture
def tv_category() -> Category:
    return Category(
        "Телевизоры",
        "Телевизор это не только передача информации, но и зомбирование населения",
        [
            "Wollmer QLED HL55 Onyx",
            "Яндекс ТВ Станция Pro YaGPT 55",
            "TCL 55C655 Pro",
            "Hisense 55U6KQ",
            "Xiaomi TV A Pro 55",
        ],
    )


@pytest.fixture
def clear_cash() -> None:
    """Фикстура обнуляет счетчики в классе Category"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def my_dict() -> dict[Any, Any]:
    return {
        "name":
            "Телевизоры",
        "description":
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "list_categ":
            ["kat1", "kat2", "kat3"],
    }


@pytest.fixture
def dict_for_json() -> list[dict[Any, Any]]:
    return [
        {
            "name": "Смартфоны",
            "description":
                "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description":
                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
