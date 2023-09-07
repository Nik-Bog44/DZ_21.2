from shop_stock.base_storage import BaseStorage
from typing import Dict

class Store(BaseStorage):
    def __init__(self, items: Dict[str, int], campacity: int = 100):
        super().__init__(items, campacity)