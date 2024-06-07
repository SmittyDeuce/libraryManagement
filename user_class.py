import re
from book_operations import book_Operations, library

class User:
    def __init__(self, name, id_num):
        self.name = name
        self.__id_num = id_num
        self.borrowed_books = []

        # Validate name format: at least two characters for both first and last name
        name_criteria = r'^[A-Za-z]{2,}\s[A-Za-z]{2,}$'
        while True:
            if re.match(name_criteria, name):
                self.name = name
                break
            else:
                print("Please Enter first and last name: min 2 char each")
                continue

        # Validate ID format: exactly 7 digits
        id_criteria = r"^\d{7}$"
        while True:
            if re.match(id_criteria, str(id_num)):
                self.__id_num = id_num
                break
            else:
                print("ID must be 7 digits")
                enter_id = input("Enter ID: ")
                if re.match(id_criteria, str(enter_id)):
                    self.__id_num = enter_id
                    break
                else:
                    print("Please enter 7 digits")
                    continue

    # Method to get the user's ID number
    def get_id(self):
        return self.__id_num

    # Method to borrow a book; triggers book_Operations with "borrow" operation
    def borrow_book(self):
        book_Operations(self, operation="borrow")

    # Method to return a book; triggers book_Operations with "return" operation
    def return_book(self):
        book_Operations(self, operation="return")

    # Method to display borrowed books
    def display_borrowed_books(self):
        if len(self.borrowed_books) <= 0:
            print(f"{self.name} has no books checked out")
        else:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print("Display:",book)


user1 = User("joe doe", 1178375)
print(user1.name)
print(user1.get_id())
user1.borrow_book()
user1.display_borrowed_books()
user1.return_book()
user1.display_borrowed_books()
