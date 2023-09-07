from typing import Dict

from exceptions import TooManyDifferentProductsError
from shop_stock.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], campacity: int = 20):
        super().__init__(items, campacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
           raise TooManyDifferentProductsError
        super().add(name, amount)