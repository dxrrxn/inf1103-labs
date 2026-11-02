from product import Product
from can_be_shipped import CanBeShipped

BASE_SHIPPING_FEE = 5.00   # dollars per order
COST_PER_KG = 2.00         # dollars per kilogram


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped. Inherits from Product, implements CanBeShipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        weight = float(weight)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()          # common info from Product
        print(f" | Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires physical shipping."

    def calculate_shipping_cost(self):
        return BASE_SHIPPING_FEE + COST_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["price"], data["stock"], data["weight"])