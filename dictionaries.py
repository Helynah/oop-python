user1 = {"userID":"0426163", "firstname": "Hellen", "lastname": "Wanyana"}

user2 = {"userID":"0394752", "firstname": "Elijah", "lastname": "Mujabi"}

user3 = {"userID":"0389435", "firstname": "Elizabeth", "lastname": "Kirabo"}

users = {"user_1":user1,"user_2":user2,"user_3":user3}

print("User's information\n")

for user, user_info in users.items():
    print(f"\nUserID: {user_info['userID']} \nFirst Name: {user_info['firstname']}\n" 
          f"Last Name: {user_info['lastname']}")
