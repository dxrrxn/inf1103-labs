import json

from product import Product

INVENTORY_FILE = "inventory.json"


def load_inventory(inventory, filename=INVENTORY_FILE):
    """Read products from the JSON file and add them to the given Inventory."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)
        print(f"{filename} found.")
        print("Inventory loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        print(f"{filename} is missing or corrupted. Starting with a new inventory.")


def save_inventory(inventory, filename=INVENTORY_FILE):
    """Write every product in the Inventory to the JSON file."""
    data = [product.to_dict() for product in inventory.get_products()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        