import pytest
from src.product import Product

@pytest.fixture
def my_phone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)