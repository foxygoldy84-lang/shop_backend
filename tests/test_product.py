from typing import Any, Dict

import pytest

from src.product import Product


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
