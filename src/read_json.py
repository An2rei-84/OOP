import json
from src.Category import Category
from src.Product import Product


def load_data_from_json(filepath):
    """Функция для чтения данных из файла json"""
    with open(filepath, 'r', encoding="UTF-8") as file:
        data = json.load(file)

    categories = {}
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(product['name'], product['description'], product['price'], product['quantity']))
        categories[category['name']] = Category(category['name'], category['description'], products)
    return categories


# print(load_data_from_json("..\\data\\products.json"))
# print(Category.product_count)
# print(Category.category_count)

