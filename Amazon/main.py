import amazon

book1 = {"author":"Hellen", "title":"Fashion and lifestyle","price":15}

book2 = {"author":"Brain", "title":"Python Crash Course","price":39}

books = [book1,book2]

prompt = input("Do you want to checkout? (yes/no): " )
if prompt.lower() ==  'yes':
    print(f"Total price: {amazon.calculate_total(books)}")
    print(f"Shipping price: {amazon.calculate_shipping(amazon.calculate_total(books))}")
else:
    print("Come back soon!")
