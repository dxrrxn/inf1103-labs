import json

from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

INVENTORY_FILE = "inventory.json"

# Maps the "type" saved in the JSON file to the class that rebuilds it.
PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}


def load_inventory(inventory: Inventory, filename: str = INVENTORY_FILE) -> None:
    """Read products from the JSON file and add the right subclass objects to the Inventory.

    Products with the same supplier ID share one Supplier object, like they did before saving.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        suppliers: dict[str, Supplier] = {}
        for item in data:
            s = item["supplier"]
            if s["id"] not in suppliers:
                suppliers[s["id"]] = Supplier(s["id"], s["name"], s["contact_email"])
            product_class = PRODUCT_TYPES[item["type"]]
            inventory.add_product(product_class.from_dict(item, suppliers[s["id"]]))
        print(f"{filename} found.")
        print("Inventory loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        print(f"{filename} is missing or corrupted. Starting with a new inventory.")


def save_inventory(inventory: Inventory, filename: str = INVENTORY_FILE) -> None:
    """Write every product in the Inventory (with its type and supplier) to the JSON file."""
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)