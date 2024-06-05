import re
from book_operations import borrow_book, return_book, display_library, search_for_book
class User:
    def __init__(self, name, id_num):

        self.name = name
        self.__id_num = id_num
        self.borrowed_books = []

        name_criteria = r'^[A-Za-z]{2,}\s[A-Za-z]{2,}$'

        while True:
            if re.match(name_criteria, name):
                self.name = name
                break
            else:
                print("Please Enter first and last name: min 2 char each")
                continue
                
        
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

    def get_id(self):
        return self.__id_num

    def borrow_book(self, title):
        borrowed = borrow_book(title)
        if borrowed:
            self.borrowed_books.append(borrowed["Title"])

    def return_book(self, title):
        returned = return_book(title)
        if returned:
            self.borrowed_books.remove(returned["Title"])

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no books checked out")
        else:
            print(f"{self.name}'s books:")
            for book in self.borrowed_books:
                print(book)

    def search_for_book(self, isbn_or_title):
        book = search_for_book(isbn_or_title)
        if book:
            print(f"Book found: {book}")
        else:
            print("Book not found.")
    



user1 = User("joe doe", 1178375)

print(user1.name)

print(user1.get_id())

user1.search_for_book("the who")
user1.display_borrowed_books()

