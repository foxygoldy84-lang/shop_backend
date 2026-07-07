from src.product import Product


class Smartphone(Product):
    """Класс-наследник для описания смартфонов."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        # Передаем базовые атрибуты в родительский класс Product
        super().__init__(name, description, price, quantity)
        # Добавляем уникальные атрибуты смартфона
        self.efficiency: float = efficiency
        self.model: str = model
        self.memory: int = memory
        self.color: str = color
