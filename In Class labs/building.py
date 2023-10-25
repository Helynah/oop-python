"""Building module"""
class Building:
    """Building class"""

    def __init__(self, name):
        self.name = name
        self._rooms = []
    
    def add_room(self,number):
        room = Room(number)
        self._rooms.append(room)

    def get_number_rooms(self):
        """returns the total number of rooms"""
        return len(self._rooms)


class Room:
    """Room class"""

    def __init__(self,number):
        """Initialize attributes of the parent class"""
        self.number = number

    

building0 = Building("Empire State Building")
building0.add_room("251")
building0.add_room("252")
print(f"\nNumber of rooms in building:  {building0.get_number_rooms()}")

