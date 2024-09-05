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
