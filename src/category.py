from typing import List

from src.product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        # [Задание 1] Сделали список товаров приватным атрибутом, чтобы к нему нельзя было получить доступ извне
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """[Задание 1] Метод для добавления объекта класса Product в приватный список товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """[Задание 2] Геттер, который возвращает все товары в виде одной большой строки."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
