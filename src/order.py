from abc import ABC, abstractmethod

from src.print_mixin import PrintMixin
from src.product import Product


class BaseGroup(ABC):
    """Абстрактный базовый класс для групп элементов (Категории, Заказы)."""

    @abstractmethod
    def __str__(self) -> str:
        """Обязательный метод для строкового отображения."""
        pass


class Order(PrintMixin, BaseGroup):
    """[Дополнительное задание] Класс для оформления заказа на один товар."""

    def __init__(self, product: Product, quantity: int) -> None:
        """[Дополнительное задание] Инициализация заказа с логированием try-else-finally."""
        try:
            if quantity <= 0:
                raise ValueError("Количество товара в заказе должно быть больше нуля.")
            if product.quantity <= 0:
                from src.exceptions import ZeroQuantityProductError

                raise ZeroQuantityProductError()
        except ValueError as e:
            print(f"Ошибка при оформлении заказа: {e}")
            raise
        else:
            self.product: Product = product
            self.quantity: int = quantity
            self.total_price: float = product.price * quantity
            super().__init__()
            print("Товар добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def __str__(self) -> str:
        """Строковое отображение заказа."""
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итого: {self.total_price} руб."
