from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A product delivered by download. Inherits from Product (no shipping)."""

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        download_size = float(download_size)
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()          # common info from Product
        print(f" | Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered digitally via download link."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data: dict, supplier: Supplier) -> "DigitalProduct":
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   supplier, data["download_size"])