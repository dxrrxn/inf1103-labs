from product import Product
from order_line import OrderLine


class Order:
    """A customer order made up of OrderLine objects.

    Composition: the Order creates its own OrderLines and manages them.
    Lines are never passed in from outside or moved to another Order.
    """

    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create a new OrderLine inside this Order (it is never created elsewhere)."""
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for this product. Returns False if there is no such line."""
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id().upper() == product_id.upper():
                self.__order_lines.remove(order_line)
                return True
        return False

    def get_order_lines(self) -> tuple[OrderLine, ...]:
        """Read-only view of the lines, so outside code can't add or move them."""
        return tuple(self.__order_lines)

    def calculate_total(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self.__order_lines)

    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        if not self.__order_lines:
            print("(no items)")
        for order_line in self.__order_lines:
            order_line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")