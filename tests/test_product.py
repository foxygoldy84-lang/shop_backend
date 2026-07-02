from typing import Any, Dict

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_data() -> Dict[str, Any]:
    return {"name": "Iphone 15", "description": "512GB", "price": 210000.0, "quantity": 8}


@pytest.fixture
def sample_product(product_data: Dict[str, Any]) -> Product:
    return Product.new_product(product_data)


def test_product_init(sample_product: Product) -> None:
    """Тест базовой инициализации продукта и геттера цены."""
    assert sample_product.name == "Iphone 15"
    assert sample_product.description == "512GB"
    assert sample_product.price == 210000.0
    assert sample_product.quantity == 8


def test_price_setter_invalid(sample_product: Product, capsys: pytest.CaptureFixture[str]) -> None:
    """Тест установки некорректной цены (менее или равна 0)."""
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 210000.0


def test_price_setter_increase(sample_product: Product) -> None:
    """Тест успешного повышения цены без лишних вопросов."""
    sample_product.price = 250000.0
    assert sample_product.price == 250000.0


def test_price_setter_decrease_confirm(
    sample_product: Product, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Тест успешного снижения цены при подтверждении пользователя ('y')."""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 190000.0
    captured = capsys.readouterr()
    assert "Цена успешно снижена" in captured.out
    assert sample_product.price == 190000.0


def test_price_setter_decrease_cancel(
    sample_product: Product, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Тест отмены снижения цены при отказе пользователя ('n')."""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 190000.0
    captured = capsys.readouterr()
    assert "Снижение цены отменено" in captured.out
    assert sample_product.price == 210000.0


def test_new_product_merge_duplicate(sample_product: Product) -> None:
    """Тест слияния дубликатов (складывание количества, выбор максимальной цены)."""
    products_list = [sample_product]
    new_data: dict[str, Any] = {"name": "Iphone 15", "description": "512GB", "price": 230000.0, "quantity": 2}

    merged_product = Product.new_product(new_data, products_list)

    assert merged_product.quantity == 10
    assert merged_product.price == 230000.0


def test_product_str(sample_product: Product) -> None:
    """Тест магического метода __str__ для продукта."""
    assert str(sample_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add(sample_product: Product) -> None:
    """Тест магического метода __add__ для сложения полной стоимости двух товаров."""
    other_product = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    # Вычисление: (210000 * 8) + (31000 * 14) = 1680000 + 434000 = 2114000
    assert sample_product + other_product == 2114000.0


def test_smartphone_init() -> None:
    """Тест инициализации смартфона и его уникальных свойств."""
    phone = Smartphone("iPhone 15", "Gray", 210000.0, 8, 3.5, "Pro", 512, "Titanium")
    assert phone.name == "iPhone 15"
    assert phone.efficiency == 3.5
    assert phone.model == "Pro"
    assert phone.memory == 512
    assert phone.color == "Titanium"


def test_lawn_grass_init() -> None:
    """Тест инициализации газонной травы и её уникальных свойств."""
    grass = LawnGrass("Трава", "Зеленая", 500.0, 10, "Россия", 14, "Светло-зеленый")
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Светло-зеленый"


def test_add_products_type_error(sample_product: Product) -> None:
    """Тест, что сложение разных классов вызывает TypeError (Задание 2)."""
    phone = Smartphone("iPhone 15", "Gray", 210000.0, 8, 3.5, "Pro", 512, "Titanium")

    with pytest.raises(TypeError):
        _ = sample_product + phone
