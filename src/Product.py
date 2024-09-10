
class Product:
    """Класс для представления продукта."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует объект Product с заданными параметрами."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Метод для строкового отображения по шаблону"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        """ Полная стоимость всех товаров на складе."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise ValueError("Оба аргумента должны быть объектами класса Product")

    @classmethod
    def new_product(cls, product_dict):
        """Создает новый объект Product из словаря параметров."""
        return cls(
            product_dict["name"],
            product_dict["description"],
            float(product_dict.get("price", 0)),
            int(product_dict.get("quantity", 0))
        )

    @property
    def price(self):
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену продукта."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
