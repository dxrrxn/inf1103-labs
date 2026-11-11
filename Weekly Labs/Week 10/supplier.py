class Supplier:
    """Represents a company that supplies products.

    Association with Product: a Supplier and a Product know about each other,
    but neither owns the other and both can exist on their own.
    """

    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id} | Name: {self.__name} | "
              f"Email: {self.__contact_email}")

    def to_dict(self) -> dict:
        """Return the supplier's data as a dictionary (used when saving to JSON)."""
        return {
            "id": self.__supplier_id,
            "name": self.__name,
            "contact_email": self.__contact_email,
        }