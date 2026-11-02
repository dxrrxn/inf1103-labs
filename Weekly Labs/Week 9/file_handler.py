import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct

INVENTORY_FILE = "inventory.json"

# Maps the "type" saved in the JSON file to the class that rebuilds it.
PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}


def load_inventory(inventory, filename=INVENTORY_FILE):
    """Read products from the JSON file and add the right subclass objects to the Inventory."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        for item in data:
            product_class = PRODUCT_TYPES[item["type"]]
            inventory.add_product(product_class.from_dict(item))
        print(f"{filename} found.")
        print("Inventory loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        print(f"{filename} is missing or corrupted. Starting with a new inventory.")


def save_inventory(inventory, filename=INVENTORY_FILE):
    """Write every product in the Inventory (including its type) to the JSON file."""
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)