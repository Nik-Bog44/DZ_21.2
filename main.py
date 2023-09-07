from exceptions import BaseError
from shop_stock.courier import Courier
from shop_stock.request import Request
from shop_stock.shop import Shop
from shop_stock.store import Store

shop = Shop(
    items={
        'печенька': 5,
        'ноутбук': 2,
        'коробки': 3,
        'собачки': 2

    })

store = Store(
    items={
        'печенька': 8,
        'ноутбук': 24,
        'коробки': 45,
        'собачки': 9
    })

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    while True:
        # TODO: Вывести содержимое складов.
        for store_name in storages:
            print(f'В {store_name} хранится: {storages[store_name].get_items()}')
        # TODO: запросить у пользователя строку.
        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "стоп" или "stop" чтобы продолжить:\n')

        if user_input in ("стоп", "stop"):
            break

        # TODO: Обработать строку
        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            # TODO: Доставить товар

            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)


if __name__ == '__main__':
    main()
