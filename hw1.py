print("Welcome to the General Provisions Store!")
prompt = "What can I get you today?"
prompt += "\n0. Food Rations: 6 gold pieces"
prompt+= "\n1. Water Flask: 3 gold pieces"
prompt += "\n2. Dagger: 12 gold pieces"
prompt += "\n3. Helmet: 32 gold pieces"
prompt += "\nEnter 0-3 of q to end> "

products = {"Food Rations" : 6, "Water Flask" : 3, "Dagger" : 12, "Helmet" : 32}
#products = ['Food Rations','Water Flask','Dagger','Helmet']

total = 0

menu = ""
while True:
    menu = input(prompt)
    if menu == 'q':
        print("\nOk, here is your receipt.")
        for choice,cost in products.items():
            if choice == choice:
                print(f"{choice} : {cost} gold pieces.")
                print(f"Thanks. Today's Total is {total} gold pieces.")
                break

    if int(menu) == 0:
        choice = "Food Rations"
        cost = 6
    elif int(menu) == 1:
        cost = 3
        choice = "Water Flask"
    elif int(menu) == 2:
        choice = "Dagger"
        cost = 12
    elif int(menu) == 3:
        choice = "Helmet"
        cost = 32 
    else:
        print("Invalid input. Enter a valid input choice or 'q' to quit\n") 
        continue

    print(f"\nGot it.You selected {choice}.")
   
    total += cost
    
    




