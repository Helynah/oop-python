"""vending machine operation"""
from vending import VendingMachine
from product import Drink
from product import Snack

# Create a vending machine
vending_machine = VendingMachine()

# Create 3 Diet Cokes
diet_coke_list = []
for i in range(3):
    diet_coke = Drink("Diet Coke")
    diet_coke_list.append(diet_coke)

# Create 2 Cliff Bars
cliff_bar_list = []
for i in range(2):
    cliff_bar = Snack("Cliff Bar")
    cliff_bar_list.append(cliff_bar)

# Stock the vending machine with various products
vending_machine.stock_item("A1", diet_coke_list, 1.50)
vending_machine.stock_item("B1", cliff_bar_list, 3.25)

# Print the inventory
vending_machine.print_inventory()

print("\n> Attempt to buy diet coke with $2.00")
(product, change) = vending_machine.purchase("A1", 2.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()

print("\n> Attempt to buy diet coke with $1.00")
(product, change) = vending_machine.purchase("A1", 1.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()

print("\n> Attempt to buy Cliff Bar with $10.00")
(product, change) = vending_machine.purchase("B1", 10.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()
