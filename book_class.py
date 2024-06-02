import re
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availabilty):

        self.title = title
        self.author = author
        self.genre = genre

        if publication_date and re.match(r'^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$', publication_date):
            print("Date syntax is valid")
            self.publication_date = publication_date
        else:
            print("Date format must be: MM-DD-YYYY")
            fix_date = input("Enter Publish Date: ")
            self.publication_date = fix_date

        if isbn and re.match(r'\d{1,}-\d{3,}-\d{5,}-\d{2,}', isbn):
            print("ISBN is valid")
            self.isbn = isbn

        else:
            print("Invalid ISBN\n")
            fix_isbn = input("Enter ISBN: ")
            self.isbn = fix_isbn
        
        if availabilty.lower() in ["yes","no"]:
            self.availability = availabilty

        else:
            print("Availability must be 'Yes' or 'No'")
            fix_availability = input("Enter Availability: ")

            while fix_availability.lower() not in ["yes","no"]:
                print("Invalid Repsonse")
                fix_availability = input("Enter Availability: ")
            self.availability = fix_availability




book1 = Book("Eggs", "suess", "123-456789-712345-67", "childrens", "8-12-1960", "maybe" )
# print(book1.availability)

# # print(book1.isbn)

# # book1.check_isbn()

# # print(book1.isbn)

# print(book1.publication_date)
