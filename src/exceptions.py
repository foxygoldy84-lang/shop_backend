class ZeroQuantityProductError(ValueError):
    """Исключение для товаров с нулевым или отрицательным количеством."""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен.") -> None:
        self.message = message
        super().__init__(self.message)
