from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface: any class that signs this contract must be able to work out a shipping cost."""

    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the shipping cost in dollars."""
        pass