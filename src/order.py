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
        self.product: Product = product
        self.quantity: int = quantity
        # Рассчитываем итоговую стоимость заказа
        self.total_price: float = product.price * quantity
        # Вызываем миксин для автоматического логирования создания заказа
        super().__init__()

    def __str__(self) -> str:
        """Строковое отображение заказа."""
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итого: {self.total_price} руб."
