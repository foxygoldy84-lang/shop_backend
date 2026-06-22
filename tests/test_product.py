import pytest

from src.product import Product


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_product_init(product_iphone: Product) -> None:
    """Тест правильной инициализации объекта класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8
