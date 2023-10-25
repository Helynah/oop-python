"""Notes module"""
class Notes:
    """Notes class"""

    def __init__(self,id,url):
        """Initialize id and url attributes"""
        self.id = id
        self.url = url

    def describe(self):
        """Simulate a notes description to a command"""
        return f"ID: {self.id} \nURL: {self.url}"
    
my_notes = Notes(426163,"http://www.mine.com/index.html")
your_notes = Notes(546372,"http://www.yours.com/index.html")
their_notes = Notes(748362,"http://www.theirs.com/index.html")

print(f"\nHellen's notes \n{my_notes.describe()}")
print(f"\nYour notes \n{your_notes.describe()}")
print(f"\nTheir notes \n{their_notes.describe()}")


class TextNote(Notes):
    """TextNote class extends Notes"""

    def __init__(self,id,url,text):
        """Initialize attributes of the parent class
        Initialize attributes specific to a text note"""
        super().__init__(id,url)
        self.text = text

    def describe(self):
        """Override the describe method"""
        return f"{super().describe()} \nText: {self.text}\n"

class PhotoNote(Notes):
    """PhotoNote class extends Notes"""

    def __init__(self,id,url,caption):
        """Initialize attributes of the parent class
        Initialize attributes specific to a text note"""
        super().__init__(id,url)
        self.caption = caption

    def describe(self):
        """Override the describe method"""
        return f"{super().describe()} \nCaption: {self.caption}"

mine = TextNote(426163,"http://www.mine.com/index.html","Good Energy")
print(f"\n{mine.describe()}")

photo = PhotoNote(426163,"http://www.mine.com/index.html","Can't complain")
print(f"\n{photo.describe()}")