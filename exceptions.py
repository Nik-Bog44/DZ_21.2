class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughSpaseError(BaseError):
    message = "Недостаточно места"


class UnknownProductError(BaseError):
    message = "Неизвестный товар"


class NotEnoughProductError(BaseError):
    message = "Не достаточно товара"


class TooManyDifferentProductsError(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequestError(BaseError):
    message = "Неправильный запрос"

class UnknownStorageError(BaseError):
    message = "Неизвестнй склад"
