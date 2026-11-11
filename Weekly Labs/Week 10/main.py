from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory, LINE
from file_handler import load_inventory, save_inventory, INVENTORY_FILE


# ---------- Input helpers ----------

def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def read_number(prompt):
    """Keep asking until the user types a non-negative number (price, weight, size)."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def read_product_type():
    while True:
        choice = input("Product type (1 = Physical, 2 = Digital): ").strip()
        if choice in ("1", "2"):
            return choice
        print("Please enter 1 or 2.")


def read_stock(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")


# ---------- Menu actions ----------

def add_product(inventory):
    print("Add New Product")
    product_id = read_non_empty("Product ID: ")
    if inventory.search_product(product_id) is not None:
        print("A product with this ID already exists.")
        return
    product_type = read_product_type()
    name = read_non_empty("Product Name: ")
    price = read_number("Price: ")
    stock = read_stock("Stock Quantity: ")

    if product_type == "1":
        weight = read_number("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = read_number("Download Size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, download_size)

    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = inventory.search_product(read_non_empty("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    product.update_stock(read_stock("New Stock Quantity: "))
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product = inventory.search_product(read_non_empty("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
    print(product.get_fulfilment_info())
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print(LINE)


def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def run_menu(inventory):
    while True:
        print_menu()
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Program exited.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = Inventory()
    load_inventory(inventory)
    run_menu(inventory)


if __name__ == "__main__":
    main()