from typing import List

from src.order import BaseGroup
from src.product import Product


class Category(BaseGroup):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        # [Задание 1] Сделали список товаров приватным атрибутом, чтобы к нему нельзя было получить доступ извне
        self.__products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """[Задание 1, продолжение] Магический метод для строкового отображения категории."""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """[Дополнительное задание] Добавление товара с логированием через try-else-finally."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Добавлять в категорию можно только продукты или их наследников")
            # Если у товара количество 0, наше исключение сработает ещё при проверке
            if product.quantity <= 0:
                from src.exceptions import ZeroQuantityProductError

                raise ZeroQuantityProductError()
        except TypeError as e:
            print(f"Ошибка типа: {e}")
            raise
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            raise
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def middle_price(self) -> float:
        """[Задание 2] Метод для подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self) -> str:
        """[Задание 2] Геттер, который возвращает все товары в виде одной большой строки."""
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result
