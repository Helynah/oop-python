fav_foods = ['matooke', 'peanut paste','chicken stew','steak','barbeque']

for fav_food in fav_foods:
    print(f"I love {fav_food}.")
 
print("\n")
for fav_food in fav_foods[1:3]:
    print(fav_food)

print("\n")
for fav_food in fav_foods[0:-1]:
    print(fav_food)

fav_foods.sort()
print("\nFoods sorted;")
print(fav_foods)

foods_upper = [fav_food.upper() for fav_food in fav_foods]
print("\nFoods in uppercase;")
print(foods_upper)