from product import Product

LINE = "-" * 60


class Inventory:
    """Groups Product objects (SRP: the collection only).

    Aggregation: the Inventory holds references to products that were created
    elsewhere. Removing a product from the Inventory does not destroy it.
    """

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Add an existing product. Returns False if a product with the same ID is already here."""
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> Product | None:
        """Take the product out of this inventory and hand it back (it still exists)."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with this ID (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().upper() == product_id.upper():
                return product
        return None

    def display_all_products(self) -> None:
        print("Current Inventory")
        print(LINE)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()      # each product decides how it displays (polymorphism)
        print(LINE)

    def get_products(self) -> list[Product]:
        """Return a copy of the product list so outside code can't change the inventory's list."""
        return list(self.__products)