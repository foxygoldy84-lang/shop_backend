from typing import Dict, List, Optional, Union


class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        # [Задание 4] Делаем цену приватным атрибутом класса
        self.__price: float = price
        self.quantity: int = quantity

    def __str__(self) -> str:
        """[Задание 1] Магический метод для строкового отображения продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """[Задание 2] Магический метод для сложения полной стоимости двух товаров на складе."""
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(
        cls, data: Dict[str, Union[str, float, int]], products_list: Optional[List["Product"]] = None
    ) -> "Product":
        """[Задание 3 + Доп. задание] Фабричный метод создания товара из словаря с проверкой дубликатов."""
        name = str(data["name"])
        description = str(data["description"])
        price = float(data["price"])
        quantity = int(data["quantity"])

        # [Доп. задание к Заданию 3] Если передан список существующих товаров, ищем дубликат по имени
        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    # Складываем количество старого и нового товара
                    existing_product.quantity += quantity
                    # При конфликте цен выбираем ту, которая является более высокой
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product

        # Если дубликат не найден, возвращаем новый объект класса Product
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """[Задание 4] Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """[Задание 4 + Доп. задание] Сеттер для установки цены с проверкой и подтверждением снижения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # [Доп. задание к Заданию 4] Если цена понижается, запрашиваем подтверждение пользователя вручную
        if new_price < self.__price:
            user_answer = input("Вы уверены, что хотите снизить цену? (y/n): ").strip().lower()
            if user_answer == "y":
                self.__price = new_price
                print("Цена успешно снижена")
            else:
                print("Снижение цены отменено")
        else:
            # Если цена повышается или не меняется, обновляем без вопросов
            self.__price = new_price
