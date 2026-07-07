import json
from pathlib import Path

from src.utils import load_data_from_json


def test_load_data_from_json(tmp_path: Path) -> None:
    """Тест корректного чтения и конвертации данных из JSON."""
    # Создаем временный тестовый JSON-файл
    test_data = [
        {
            "name": "Продукты",
            "description": "Еда",
            "products": [{"name": "Хлеб", "description": "Белый", "price": 50.0, "quantity": 10}],
        }
    ]
    file = tmp_path / "test_products.json"
    file.write_text(json.dumps(test_data), encoding="utf-8")

    # Запускаем функцию
    categories = load_data_from_json(str(file))

    assert len(categories) == 1
    assert categories[0].name == "Продукты"

    # Проверяем, что строковый геттер содержит наш товар
    assert "Хлеб, 50.0 руб. Остаток: 10 шт.\n" in categories[0].products
