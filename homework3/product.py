"""Product module"""


class Product:
    """Product class"""

    def __init__(self, product_name):
        """initialize the attributes"""
        self.product_name = product_name

    def consume(self):
        """consume the product"""
        print("Sorry, this product is empty.")


class Drink(Product):
    """Drink class"""

    def consume(self):
        """simulate a consume method to the command"""
        print(f"Yum, you drink the {self.product_name}.")


class Snack(Product):
    """Snack class"""

    def consume(self):
        """simulate a consume method to the command"""
        print(f"Yum, you eat the {self.product_name}.")
