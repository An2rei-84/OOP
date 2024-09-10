from src.Category import Category
from src.smartphone import Smartphone
import unittest


class TestSmartphone(unittest.TestCase):
    def test_smartphone_model(self):
        smartphone = Smartphone("Смартфон", "Описание смартфона", 0, 1, 5000,
                                "Модель", "16", "Grey")
        result = smartphone.model
        self.assertEqual(result, "Модель")

    def test_empty_list(self):
        category = Category("Другое", "Здесь ничего не продаётся", [])
        result = category.__str__()
        expected_result = 'Другое, Количество продуктов: 0 шт.'
        self.assertEqual(result, expected_result)
