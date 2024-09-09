import unittest
from src.Category import Category
from src.Product import Product


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.products = [self.product1, self.product2, self.product3]

    def test_init(self):
        products = [self.product1, self.product2, self.product3]
        category = Category("Смартфоны",
                            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                            products)
        assert category.name == "Смартфоны"
        assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        self.assertIsInstance(category.products, str)

    def test_products(self):
        product1 = Product("Телевизор", "4K", 10000, 8)
        product2 = Product("Смартфон", "100MP", 5000,9)
        category = Category("Электроника", "Различные электронные устройства", [product1, product2])
        expected_category = Category('Электроника', 'Различные электронные устройства', [product1, product2])

        self.assertCountEqual(category.products, expected_category.products)
        self.assertEqual(category.name, expected_category.name)
        self.assertEqual(category.description, expected_category.description)

    def test_products_property(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        products = [product1, product2, product3]
        category = Category("Смартфоны",
                            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                            products)

        expected_output = "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in products]).strip()
        actual_output = category.products.strip()

        self.assertEqual(actual_output, expected_output)

    def test_add_product(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        products = [product1, product2, product3]
        category = Category("Смартфоны",
                            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                            products)

        new_product = Product("Huawei P50 Pro", "128GB, Черный", 90000.0, 10)
        category.add_product(new_product)

        self.assertEqual(Category.product_count, len(products))

    def test_str(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        products = [product1, product2, product3]
        category = Category("Смартфоны",
                            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                            products)

        expected_output = f"Смартфоны, Количество продуктов: 27 шт."
        actual_output = str(category)
        self.assertEqual(expected_output, actual_output)

