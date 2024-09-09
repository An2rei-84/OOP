
class Category:
    """Класс для представления категории продуктов."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализирует объект Category с заданными параметрами."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в данную категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Формирует строку с информацией о продуктах в данной категории."""
        products_string = ""
        for product in self.__products:
            products_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_string
