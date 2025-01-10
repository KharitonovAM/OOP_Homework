class Category:
    '''Класс по созданию объектов Category'''

    name: str
    description: str
    products: list
    count_names = 0

    def __init__(self, name, description, products):
        '''Инициализация объекта класса Category'''

        self.name = name
        self.description = description
        self.products = products
        Category.count_names += len(products)

