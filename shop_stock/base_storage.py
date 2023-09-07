from typing import Dict

from exceptions import NotEnoughSpaseError, UnknownProductError, NotEnoughProductError
from shop_stock.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], campacity: int):
        self._items = items
        self._campacity = campacity

    def add(self, name: str, amount: int) -> None:

        if self.get_free_space() < amount:
            raise NotEnoughSpaseError
        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self._items:
            raise UnknownProductError
        if self._items.get(name, 0) < amount:
            raise NotEnoughProductError
        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)


    def get_free_space(self) -> int:
        return self._campacity - sum(self._items.values())

    def get_items(self) -> Dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
