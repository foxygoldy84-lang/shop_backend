import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_xiaomi() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 310000.0, 14)


def test_product_init(product_iphone: Product) -> None:
    """Тест правильной инициализации объекта класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_category_init(product_iphone: Product, product_xiaomi: Product) -> None:
    """Тест правильной инициализации объекта класса Category."""
    # Сбрасываем счетчики перед тестом, так как они статические
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        "Смартфоны",
        "Мобильные телефоны",
        [product_iphone, product_xiaomi]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2
