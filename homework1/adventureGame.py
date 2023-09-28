#Hellen M Wanyana
#CSC-287-01

locations = {
    "garden":{"description":"You are in the garden.",
             "exits":{"east":"kitchen"},"look":"You are standing in a large garden.\
            \nYou can see beautiful flowers all around.\nThere is a small house to the east."
             },
    "kitchen":{"description":"You are in the kitchen.",
           "exits":{"west":"garden", "east":"living room","south":"dining room","north":
                    "master bedroom"},
           "look":"You are standing in the kitchen.\nIt's a mess in here!\
            \nYou can see a garden to the west,and living room to the east."
           },
    "master bedroom":{"description":"You are in the master bedroom.", "exits":{"north":"attic",
            "south":"kitchen"},"look":"It's cozy in here. Relax and feel comfortable.You can go up \
to the attic to see some treasures."},
    "attic":{"description":"You are in the attic.","exits":{"south":"master bedroom"},"look":
    "There is some hidden treasures in here. You have to go through the bedroom to find your way \
back."},
    "living room":{"description":"You are in the living room.","exits":{"west":"kitchen",
           "east":"small bedroom","north":"porch","south":"study room"},"look":"You are standing\
in the living room and it is the heart of a home. It is enveloped with comfort and coziness.\
\nFamily and friends usually gather for thanksgiving and social events. \
\nThe most memorable moments are made here."},
    "small bedroom":{"description":"You are in a small bedroom.","exits":{"west":"living room",},
            "look":"You are standing in a small bedroom(guest bedroom).It is a place of quiet \
retreat,sanctuary where visitors can relax, and enjoy a peaceful night's sleep."},
    "porch":{"description":"You are standing at the porch.", "exits":{"south":"living room"},"look":
             "The porch is one of my favorites.\nIt has a swaying swing where one can watch the\
birds from while enjoying the breeze."},
    "dining room":{"description":"You are in the dining room.","exits":{"north":"kitchen","east":
            "study room"},"look":"The walls of the dining room are adorned with tasteful artwork. \
    \nIt is an inviting space designed for sharing meals and creating lasting memories with family \
and friends."},
    "study room":{"description":"You are in the study room.","exits":{"west":"dining room","north":
            "living room"},"look":"The walls of the study room are framed with inspirational \
quotes.\nThis is a dedicated space for focused work, learning,and intellectual pursuits."} }    

def house_map():
    """Describing the room locations in the house"""
    print("This is how to go about your way in this house.")
    print("From the garden, East = Kitchen.\nFrom the kitchen, East = Living Room, West = Garden, \
North = Master bedroom, South = Dining room \nFrom the living room, East = Small bedroom, \
South = Study room, North = porch \nFrom the master bedroom, North = attic" )
    print("Select a direction of the room you would like to go to depending on the room you are in.\
\n*Enter 'look' to see what happens in that room. \n*Enter quit when you are done with the house \
tour.")

#current_location = "garden"

#def move(current_location):
    

    #if location == locations[current_location]:
        #print(locations["description"])
    #elif  current_location in location[current_location]:
        #location = locations[current_location]["exits"]

house_map()

print("\n\nYou are standing in a large garden.\nYou can see beautiful flowers all around.\
\nThere is a small house to the east.")
current_location = "garden"    

#direction = input("> ").lower()

#move(locations)


while current_location != "quit":
    location = locations[current_location]
    print(location["description"])

    direction = input("> ").lower()

    if direction == "quit":
        print("Thanks for touring my home!")
        break

    if direction == "look":
        print(location["look"])

    if direction in location["exits"]:
        current_location = location["exits"][direction]
    else:
        print("You can not go that way. Read the map carefully and input a new direction")

    
