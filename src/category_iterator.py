from typing import Any

from src.category import Category


class CategoryIterator:
    """[Дополнительное задание] Класс для перебора товаров категории в цикле for."""

    def __init__(self, category: Category) -> None:
        # Получаем доступ к приватному списку товаров категории через трюк Name Mangling
        # Так как список приватный (__products), Python переименовывает его внутри в _Category__products
        self.products = getattr(category, "_Category__products")
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает сам объект-итератор."""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Возвращает следующий продукт из категории или останавливает цикл."""
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
