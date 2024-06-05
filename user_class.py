import re
from book_operations import book_Operations,library
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

    def borrow_book(self):
        book_Operations()

        title = input("Enter title of book to borrow: ")

        for isbn, details in library.items():
            if title.lower() == details["Title"].lower():
                if details["Availability"].lower() == 'yes':
                    self.borrowed_books.append(details["Availability"])
                    details["Availability"] = 'no'
                    print(f"{self.name} checked out {title}")
                    return
                
                else:
                    print(f"{title} not available")
                    return
    

    def display_borrowed_books(self):
        if len(self.borrowed_books) <= 0:
            print(f"{self.name} has no books checked out")

        else:
            print(f"{self.name}'s borrowed books:")
            print(self.borrowed_books)
      




user1 = User("joe doe", 1178375)

print(user1.name)

print(user1.get_id())

user1.borrow_book()
user1.display_borrowed_books()

