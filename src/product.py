class Product:
    """Класс по созданию объектов Продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        '''Инициализация объекта класса Product'''
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity