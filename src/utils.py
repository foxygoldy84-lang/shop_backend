import json
from typing import List

from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> List[Category]:
    """Функция для чтения JSON-файла и конвертации данных в объекты классов."""
    categories: List[Category] = []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        for category_data in data:
            products_list: List[Product] = []
            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
                products_list.append(product)

            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products_list,
            )
            categories.append(category)

    return categories
