from typing import List

import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
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


def test_category_str(sample_products: List[Product]) -> None:
    """Тест магического метода __str__ для категории."""
    category = Category("Смартфоны", "Телефоны", sample_products)
    # Проверяем суммирование остатков на складе: 8 + 14 = 22
    assert str(category) == "Смартфоны, количество продуктов: 22 шт."


def test_category_iterator(sample_products: List[Product]) -> None:
    """Тест класса-итератора для перебора товаров категории в цикле for."""
    category = Category("Смартфоны", "Телефоны", sample_products)
    iterator = CategoryIterator(category)

    # Собираем элементы итератора обратно в список
    iterated_products = list(iterator)

    assert len(iterated_products) == 2
    assert iterated_products[0].name == "Iphone 15"
    assert iterated_products[1].name == "Xiaomi Redmi Note 11"


def test_category_add_product_invalid() -> None:
    """Тест, что добавление чужого объекта вызывает TypeError (Задание 3)."""
    category = Category("Смартфоны", "Телефоны", [])

    with pytest.raises(TypeError):
        category.add_product("Не продукт, а просто строка")  # type: ignore
