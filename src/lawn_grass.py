from src.product import Product


class LawnGrass(Product):
    """Класс-наследник для описания газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        # Передаем базовые атрибуты в родительский класс Product
        super().__init__(name, description, price, quantity)
        # Добавляем уникальные атрибуты газонной травы
        self.country: str = country
        self.germination_period: int = germination_period
        self.color: str = color
