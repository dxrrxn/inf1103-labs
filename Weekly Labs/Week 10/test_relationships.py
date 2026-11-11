"""Lab 8 tests: association, aggregation, composition, LSP and polymorphism.

Run with:  python3 test_relationships.py
Each section prints what happened so you can compare it with your "Predict first" notes.
"""
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def heading(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def show_product_details(product: Product) -> None:
    """Works with ANY Product: it only uses what every Product promises."""
    product.display_information()
    print(product.get_fulfilment_info())


def test_association() -> None:
    heading("2. ASSOCIATION: Supplier <-> Product")
    supplier = Supplier("S001", "Music World", "sales@musicworld.com")
    guitar = PhysicalProduct("P001", "Guitar", 350, 5, supplier, 3.5)
    windows = DigitalProduct("D001", "Windows 11", 199, 100, supplier, 5400)

    print("Supplier info through each product:")
    guitar.get_supplier().display_information()
    windows.get_supplier().display_information()
    print("Supplier and product are separate objects:", supplier is not guitar)
    print("Both products share the same Supplier object:",
          guitar.get_supplier() is windows.get_supplier())

    print("\nPredict first: after `del supplier`, can the products still show it?")
    del supplier
    guitar.get_supplier().display_information()
    windows.get_supplier().display_information()
    print("Yes - `del` only removes the variable name. The products still hold "
          "a reference, so the Supplier object still exists.")


def test_aggregation() -> None:
    heading("3. AGGREGATION: Inventory <>-- Product")
    supplier = Supplier("S002", "Tech Supplies", "hello@techsupplies.com")
    mouse = PhysicalProduct("P002", "Mouse", 25.5, 40, supplier, 0.2)
    print("Product created BEFORE any inventory exists:")
    mouse.display_information()

    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(mouse)
    print("\nAdded to Inventory A. Found in A:", inventory_a.find_product("P002") is mouse)

    print("\nPredict first: does the product still work after removing it from A?")
    removed = inventory_a.remove_product("P002")
    print("Removed from A. Still in A?", inventory_a.find_product("P002") is not None)
    print("Removed object is the same product:", removed is mouse)
    mouse.update_stock(35)
    mouse.display_information()
    print("Yes - the Inventory only dropped its reference; the Product was not destroyed.")

    inventory_b.add_product(mouse)
    print("\nTransferred to Inventory B. Found in B:", inventory_b.find_product("P002") is mouse)
    inventory_b.display_all_products()
    inventory_a.display_all_products()


def test_composition() -> None:
    heading("4. COMPOSITION: Order <>== OrderLine")
    supplier = Supplier("S001", "Music World", "sales@musicworld.com")
    guitar = PhysicalProduct("P001", "Guitar", 350, 5, supplier, 3.5)
    windows = DigitalProduct("D001", "Windows 11", 199, 100, supplier, 5400)

    order_1 = Order("O001")
    order_1.add_order_line(guitar, 2)
    order_1.add_order_line(windows, 1)
    order_1.display_order()

    print("\nPredict first: add the same Guitar to a second Order.")
    print("How many OrderLine objects and Product objects?")
    order_2 = Order("O002")
    order_2.add_order_line(guitar, 1)
    order_2.display_order()

    line_1 = order_1.get_order_lines()[0]
    line_2 = order_2.get_order_lines()[0]
    print("Same OrderLine object in both orders?", line_1 is line_2)
    print("OrderLine ids:", id(line_1), id(line_2))
    print("Same Product object in both lines?", line_1.get_product() is line_2.get_product())
    print("Product ids:", id(line_1.get_product()), id(line_2.get_product()))
    print("=> 2 OrderLine objects (one per Order), but only 1 Guitar Product.")

    print("\nRemoving the Windows line from Order O001:")
    order_1.remove_order_line("D001")
    order_1.display_order()
    print("The Windows product still exists:", windows.get_name())

    print("\nRemoving Order O002 from the scenario:")
    del order_2
    print("Its OrderLine went with it (nothing else manages it), "
          "but the Guitar product is still here:", guitar.get_name())


def test_lsp_and_polymorphism() -> None:
    heading("6 & 7. LSP AND POLYMORPHISM through the Product type")
    supplier = Supplier("S001", "Music World", "sales@musicworld.com")
    products: list[Product] = [
        PhysicalProduct("P001", "Guitar", 350, 5, supplier, 3.5),
        DigitalProduct("D001", "Windows 11", 199, 100, supplier, 5400),
    ]

    print("show_product_details() called with each product, function unchanged:")
    for product in products:
        show_product_details(product)

    print("\nPredict first: what does get_fulfilment_info() print for each product?")
    inventory = Inventory()
    for product in products:
        inventory.add_product(product)
    for product in inventory.get_products():          # one loop, no isinstance()
        product.display_information()
        print(product.get_fulfilment_info())

    print("\nLSP check: update_stock() means the same thing for both subclasses.")
    for product in inventory.get_products():
        product.update_stock(10)
        print(f"{product.get_name()} stock is now {product.get_stock()}")
        try:
            product.update_stock(-1)
        except ValueError as error:
            print(f"{product.get_name()} rejects -1 the same way: {error}")


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_and_polymorphism()