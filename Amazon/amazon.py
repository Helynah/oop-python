#book1 = {"author":"Hellen", "title":"Fashion and lifestyle","price":15}

#book2 = {"author":"Brain", "title":"Python Crash Course","price":39}

#books = [book1,book2]


def calculate_total(bookie):
    """calculate the total of the books"""
    return sum(book["price"] for book in bookie)

def calculate_shipping(total_price):
    """Determines the shipping price"""
    if total_price > 100:
        return 0.00
    else:
        return 3.99
#prompt = input("Do you want to checkout? (yes/no): " )
#def checkout()
#if prompt.lower() ==  'yes':
    #print(f"Total price: {calculate_total(bookie)}")
    #print(f"Shipping price: {calculate_shipping(calculate_total(bookie))}")
#else:
#   print("Come back soon!")
