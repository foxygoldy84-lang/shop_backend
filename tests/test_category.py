import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products() -> list[Product]:
    return [
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 310000.0, 14),
    ]


def test_category_init(sample_products: list[Product]) -> None:
    """Тест правильной инициализации объекта класса Category."""
    # Сбрасываем счетчики перед тестом, так как они глобальные для класса
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Мобильные телефоны", sample_products)

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2
