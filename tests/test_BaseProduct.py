import unittest
from src.BaseProduct import BaseProduct


class TestBaseProduct(unittest.TestCase):
    def test_abstract_method(self):
        with self.assertRaises(TypeError):
            base_product = BaseProduct()
            print(base_product.__str__())
