"""vending module"""
from product import Product


class VendingMachine:
    """Vending machine class"""

    def __init__(self):
        """Initialize the attributes"""
        self._slots = {}
        self.total_sales = 0

    def stock_item(self, location, product_list, unit_price):
        """stocks a list of products to a slot location with their unit price"""
        self._slots[location] = Slot(product_list, unit_price)
        #allocate the product_list with its unit price to a slot location

    def print_inventory(self):
        """prints out all the inventory"""
        #loop through the slots dictionary to print out the product_list items for each location
        for location, slot in self._slots.items():
            print(location)
            for product in slot.product_list:
                print(f"- {product.product_name}")

    def purchase(self, location, deposit):
        """returns a tuple with a product purchased and change"""
        slot = self._slots.get(location)

        unit_price = slot.get_unit_price()
        if unit_price > deposit:
            return Product("Empty Product"), deposit
        else:
            product = slot.product_list.pop() #remove the product
            self.total_sales += unit_price #update the total sales
            return product, deposit - unit_price #return the product purchased and the change


class Slot:
    """slot class"""

    def __init__(self, product_list, _unit_price):
        """Initialize the Slot attributes"""
        self.product_list = product_list
        self._unit_price = _unit_price

    def get_unit_price(self):
        """Returns the unit price of products in this slot."""
        return self._unit_price
