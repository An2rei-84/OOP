
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
