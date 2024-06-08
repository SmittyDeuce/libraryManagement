import re

class User():
    name_criteria = r'^[a-zA-Z]{2,} [a-zA-Z]{2,}$'
    id_criteria = r'^\d{7}$'

    def __init__(self, name, id):
        
        if not re.match(self.name_criteria, name):
            raise ValueError("First and Last name must\nbe at least two Letters Long")
        
        if not re.match(self.id_criteria, str(id)):
            raise ValueError("ID must be 7 digits long")
        
        self.name = name
        self.id = id
        self.borrowed_books = []


        
# user1 = User("Joe doe",7896543)
