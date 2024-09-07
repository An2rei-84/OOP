import unittest
from unittest import mock
from src.Category import Category
from src.Product import Product


class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):
        self.category_name = "Смартфоны"
        self.category_description = "Описание категории смартфонов"
        self.product_name = "Samsung Galaxy S23 Ultra"
        self.product_description = "Описание продукта Samsung Galaxy S23 Ultra"
        self.product_price = 180000.0
        self.product_quantity = 5

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='{"name": "Смартфоны", "description": "Описание категории смартфонов", "products": [{"name": "Samsung Galaxy S23 Ultra", "description": "Описание продукта Samsung Galaxy S23 Ultra", "price": 180000.0, "quantity": 5}]}')
    def test_category_init(self, mock_open):
        category = Category(self.category_name, self.category_description, [])
        self.assertEqual(category.name, self.category_name)
        self.assertEqual(category.description, self.category_description)
        self.assertListEqual(category.products, [])

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='{"name": "Samsung Galaxy S23 Ultra", "description": "Описание продукта Samsung Galaxy S23 Ultra", "price": 180000.0, "quantity": 5}')
    def test_product_init(self, mock_open):
        product = Product(self.product_name, self.product_description, self.product_price, self.product_quantity)
        self.assertEqual(product.name, self.product_name)
        self.assertEqual(product.description, self.product_description)
        self.assertAlmostEqual(product.price, self.product_price)
        self.assertEqual(product.quantity, self.product_quantity)

    def test_category_count(self):
        category = Category(self.category_name, self.category_description, [])
        self.assertEqual(category.category_count, 1)

    def test_product_count(self):
        category = Category(self.category_name, self.category_description, [])
        product = Product(self.product_name, self.product_description, self.product_price, self.product_quantity)
        category.products.append(product)
        self.assertEqual(category.product_count, 0)


def test_new_product():
    product_dict = {'name': 'Банан', 'description': 'Жёлтый банан', 'price': 20, 'quantity': 20}
    product = Product.new_product(product_dict)
    assert product.name == 'Банан'
    assert product.description == 'Жёлтый банан'
    assert product.price == 20
    assert product.quantity == 20


def test_valid_prices():
    product = Product('Яблоко', 'Зелёное яблоко', 50, 10)
    product.price = 70
    assert product.price == 70


def test_add_product():
    category = Category('Яблоко', 'Зелёное яблоко', [Product('Яблоко', 'Зелёное яблоко', 50, 10)])

    category.add_product(Product('Красные яблоки', 'Яблоко', 70, 5))

    assert len(category.products) == 2
    assert category.product_count == 2


def test_new_list_products():
    category = Category('Яблоко', 'Зелёное яблоко', [
        Product('Яблоко', 'Зелёное яблоко', 50, 10),
        Product('Красные яблоки', 'Яблоко', 70, 5),
        Product('Банан', 'Жёлтые бананы', 30, 15)
    ])

    expected_products = """Яблоко, 50 руб. Остаток: 10 шт.
Красные яблоки, 70 руб. Остаток: 5 шт.
Банан, 30 руб. Остаток: 15 шт.\n"""

    actual_products = category.new_list_products()
    assert actual_products == expected_products
