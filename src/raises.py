class ZeroQuantityError(Exception):
    """Класс обработки ошибок при добавлении продукта с количествоим 0"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Пытались добавить продукт с количеством 0"

    def __str__(self):
        return self.message
