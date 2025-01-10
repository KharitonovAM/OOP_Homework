class Category:
    '''Класс по созданию объектов Category'''

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products) -> None:
        '''Инициализация объекта класса Category'''

        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1

