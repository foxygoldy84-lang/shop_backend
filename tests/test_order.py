from src.order import Order
from src.product import Product


def test_order_init() -> None:
    """Тест создания заказа, подсчета стоимости и строкового вывода."""
    product = Product("Тестовый товар", "Описание", 100.0, 10)
    order = Order(product, 3)

    assert order.product == product
    assert order.quantity == 3
    assert order.total_price == 300.0
    order_str = str(order)
    assert "Заказ:" in order_str
    assert "Тестовый товар" in order_str
    assert "300.0" in order_str
    assert "Order" in repr(order)
