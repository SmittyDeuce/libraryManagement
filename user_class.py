import re

# Define the User class
class User():
    # Define regular expression patterns for name and ID validation
    name_criteria = r'^[a-zA-Z]{2,} [a-zA-Z]{2,}$'  # Matches names with at least two letters each for first and last name
    id_criteria = r'^\d{7}$'  # Matches IDs with exactly 7 digits
    
    # Initialize the User object with a name, ID, and an empty list for borrowed books
    def __init__(self, name, id):
        # Validate the name using regular expression
        if not re.match(self.name_criteria, name):
            raise ValueError("First and Last name must\nbe at least two Letters Long")
        
        # Validate the ID using regular expression
        if not re.match(self.id_criteria, str(id)):
            raise ValueError("ID must be 7 digits long")
        
        # Assign the name, ID, and an empty list for borrowed books to the object's attributes
        self.name = name
        self.id = id
        self.borrowed_books = []


        
# user1 = User("Joe doe",7896543)
