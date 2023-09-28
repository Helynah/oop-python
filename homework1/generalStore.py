#Hellen M Wanyana
#CSC-287-01

#print the store's inventory
print("Welcome to the General Provisions Store!")
PROMPT = "What can I get you today?"\
"\n0. Food Rations: 6 gold pieces \n1. Water Flask: 3 gold pieces"\
"\n2. Dagger: 12 gold pieces \n3. Helmet: 32 gold pieces \nEnter 0-3 of q to end> "

products = ['Food Rations','Water Flask','Dagger','Helmet']#list of products sold

cost = [6,3,12,32]#list of the cost of the products

def total_cost(choices):
    """
    calculates the total cost of all goods selected by the customer
    """
    total = 0
    for item in choices:
        total += cost[item]
    return total

choices = []#An empty list to store the customer's choices

while True:
    menu = input(PROMPT)
    if menu == 'q':
        print("\nOk, here is your receipt.")
        for choice in choices:
            print(f"{products[choice]} : {cost[choice]} gold pieces.")
        print(f"Thanks. Today's Total is {total_cost(choices)} gold pieces.")
        break
    index = int(menu)
    if index in range (4):
        choices.append(index)#added index of the customer's choices to the choices list
        print(f"\nGot it. You selected {products[index]}.")
    else:
        print("Invalid input. Enter a valid input choice or 'q' to quit\n")
        continue



