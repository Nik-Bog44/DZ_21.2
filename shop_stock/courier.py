from typing import Dict

from shop_stock.abstract_storage import AbstractStorage
from shop_stock.request import Request

class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__from_storage = storages[self.__request.departure]
        self.__to_storage = storages[self.__request.destination]

    def move(self):
        self.__from_storage.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.product} {self.__request.amount} из {self.__request.departure}')

        print(f'Курьер везёт {self.__request.product} {self.__request.amount}')

        self.__to_storage.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.product} {self.__request.amount} в {self.__request.destination}')

    def cancel(self):
        self.__from_storage.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер вернул {self.__request.product} {self.__request.amount} в {self.__request.departure}')