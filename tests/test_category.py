from typing import List

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products() -> List[Product]:
    return [Product("Iphone 15", "512GB", 210000.0, 8), Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)]


def test_category_init(sample_products: List[Product]) -> None:
    """Тест правильной инициализации и строкового геттера продуктов в формате Задания 2."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Телефоны", sample_products)

    assert category.name == "Смартфоны"
    assert category.description == "Телефоны"

    # Проверяем работу строкового геттера продуктов (Задание 2)
    expected_string = "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    assert category.products == expected_string
