from src.Product import Product


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Невозможно добавить объект, не являющийся продуктом")

    @property
    def products(self):
        """Формирует строку с информацией о продуктах в данной категории."""
        products_string = ""
        for product in self.__products:
            products_string += f"{product}"
        return products_string

    def __str__(self):
        """ Рассчитывает общее количество товаров на складе (quantity)
            для каждого продукта в приватном атрибуте products"""

        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, Количество продуктов: {total_quantity} шт."
