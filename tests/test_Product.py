from src.Product import Product
import unittest


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


class TestProduct(unittest.TestCase):
    def test_addition(self):
        product1 = Product('Яблоко', 'Зелёное яблоко', 50, 10)
        product2 = Product('Апельсин', 'Оранжевый апельсин', 20, 5)
        expected_result = 50 * 10 + 20 * 5
        result = product1 + product2
        self.assertEqual(expected_result, result)

    def test_str(self):
        product = Product('Яблоко', 'Зелёное яблоко', 50, 10)
        expected_output = "Яблоко, 50 руб. Остаток: 10 шт.\n"
        actual_output = str(product)
        self.assertEqual(expected_output, actual_output)
