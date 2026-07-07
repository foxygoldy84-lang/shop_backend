from typing import Any


class PrintMixin:
    """Миксин для автоматического вывода информации о создании объекта в консоль."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # Сначала вызываем инициализацию следующего класса в цепочке наследования
        super().__init__(*args, **kwargs)
        # Печатаем информацию о созданном объекте, используя repr самого себя
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта в виде ИмяКласса(аргументы)."""
        # Собираем все свойства объекта, кроме приватных (начинающихся с подчёркивания)
        props = []
        for key, value in self.__dict__.items():
            # Убираем системные префиксы Name Mangling типа _Category__products или _Product__price
            display_key = key.split("__")[-1]
            if not display_key.startswith("_"):
                props.append(f"{display_key}={repr(value)}")

        # Склеиваем их через запятую
        props_str = ", ".join(props)
        return f"{self.__class__.__name__}({props_str})"
