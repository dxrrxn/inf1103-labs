from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory, LINE
from order import Order
from file_handler import load_inventory, save_inventory, INVENTORY_FILE


# ---------- Input helpers ----------

def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def read_number(prompt: str) -> float:
    """Keep asking until the user types a non-negative number (price, weight, size)."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def read_stock(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")


def read_quantity(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Quantity must be at least 1.")
        except ValueError:
            print("Please enter a whole number.")


def read_product_type() -> str:
    while True:
        choice = input("Product type (1 = Physical, 2 = Digital): ").strip()
        if choice in ("1", "2"):
            return choice
        print("Please enter 1 or 2.")


# ---------- Supplier lookup ----------

def find_supplier(inventory: Inventory, supplier_id: str) -> Supplier | None:
    """Reuse a Supplier object that an existing product already refers to."""
    for product in inventory.get_products():
        supplier = product.get_supplier()
        if supplier.get_supplier_id().upper() == supplier_id.upper():
            return supplier
    return None


def read_supplier(inventory: Inventory) -> Supplier:
    supplier_id = read_non_empty("Supplier ID: ")
    supplier = find_supplier(inventory, supplier_id)
    if supplier is not None:
        print(f"Using existing supplier: {supplier.get_name()}")
        return supplier
    name = read_non_empty("Supplier Name: ")
    email = read_non_empty("Supplier Email: ")
    return Supplier(supplier_id, name, email)


# ---------- Menu actions ----------

def add_product(inventory: Inventory) -> None:
    print("Add New Product")
    product_id = read_non_empty("Product ID: ")
    if inventory.find_product(product_id) is not None:
        print("A product with this ID already exists.")
        return
    product_type = read_product_type()
    name = read_non_empty("Product Name: ")
    price = read_number("Price: ")
    stock = read_stock("Stock Quantity: ")
    supplier = read_supplier(inventory)

    product: Product
    if product_type == "1":
        weight = read_number("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, supplier, weight)
    else:
        download_size = read_number("Download Size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, supplier, download_size)

    inventory.add_product(product)
    print("Product added successfully!")


def remove_product(inventory: Inventory) -> None:
    print("Remove Product")
    product = inventory.remove_product(read_non_empty("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print(f"{product.get_name()} removed from the inventory.")


def update_stock(inventory: Inventory) -> None:
    print("Update Stock")
    product = inventory.find_product(read_non_empty("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    product.update_stock(read_stock("New Stock Quantity: "))
    print("Stock updated successfully!")


def search_product(inventory: Inventory) -> None:
    print("Search Product")
    product = inventory.find_product(read_non_empty("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
    print(product.get_fulfilment_info())
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    product.get_supplier().display_information()
    print(LINE)


def create_order(inventory: Inventory) -> None:
    print("Create Order")
    order = Order(read_non_empty("Order ID: "))
    while True:
        product_id = input("Product ID to add (leave blank to finish): ").strip()
        if not product_id:
            break
        product = inventory.find_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        order.add_order_line(product, read_quantity("Quantity: "))
        print(f"Added {product.get_name()}.")
    print(LINE)
    order.display_order()
    print(LINE)


def print_menu() -> None:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Update Stock")
    print("5. Search Product")
    print("6. Create Order")
    print("7. Save Inventory")
    print("8. Exit")
    print("----------------------------")


def run_menu(inventory: Inventory) -> None:
    while True:
        print_menu()
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all_products()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            remove_product(inventory)
        elif option == "4":
            update_stock(inventory)
        elif option == "5":
            search_product(inventory)
        elif option == "6":
            create_order(inventory)
        elif option == "7":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")
        elif option == "8":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Program exited.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 8.")


def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = Inventory()
    load_inventory(inventory)
    run_menu(inventory)


if __name__ == "__main__":
    main()