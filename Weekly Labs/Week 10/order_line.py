from product import Product


class OrderLine:
    """One product and the quantity ordered, inside an Order.

    Composition: an OrderLine is created by, and belongs to, exactly one Order.
    Association: it refers to a Product but does not own it.
    """

    def __init__(self, product: Product, quantity: int):
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__product.get_product_id()} | {self.__product.get_name()} | "
              f"{self.__quantity} x ${self.__product.get_price():.2f} = "
              f"${self.calculate_subtotal():.2f}")