from src.Product import Product


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

