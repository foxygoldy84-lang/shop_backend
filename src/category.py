from typing import List

from src.product import Product


class Category:
    # Атрибуты класса для подсчета количества категорий и уникальных товаров
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products

        # Увеличиваем счетчик категорий при создании нового объекта
        Category.category_count += 1
        # Увеличиваем счетчик уникальных товаров на количество элементов в переданном списке
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в категорию."""
        self.products.append(product)
        Category.product_count += 1
