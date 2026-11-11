from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    """Abstract base class for every product (SRP: one product only).

    A plain Product can't be created; use PhysicalProduct or DigitalProduct.
    """

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = float(price)
        self.__stock: int = 0
        self.__supplier: Supplier = supplier      # association: a reference, not ownership
        self.update_stock(stock)

    # ---------- Read-only access to attributes ----------

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    # ---------- Behaviour ----------

    def update_stock(self, quantity: int) -> None:
        """Set the stock level. Every product accepts any whole number from 0 upwards."""
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock} | "
              f"Supplier: {self.__supplier.get_name()}", end="")

    def to_dict(self) -> dict:
        """Return the product's common data as a dictionary (used when saving to JSON)."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return a message describing how this product reaches the customer."""
        pass