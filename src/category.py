class Category:
    '''Класс по созданию объектов Category'''

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        '''Инициализация объекта класса Category'''

        self.name = name
        self.description = description
        self.products = products

