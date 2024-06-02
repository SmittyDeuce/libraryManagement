import re
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availabilty):

        self.title = title
        self.author = author
        self.genre = genre
        
        publication_date_criteria = re.match(r'^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$', publication_date)

        if publication_date and publication_date_criteria:
            print("Date syntax is valid")
            self.publication_date = publication_date
        else:
            print("Date format must be: MM-DD-YYYY")
            while True:
                fix_date = input("Enter Publish Date: ")
                if re.match(r'^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$', fix_date):
                    self.publication_date = fix_date
                    break
                else:
                    print("Invalid Format")
                    continue

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
            while True:

                fix_availability = input("Enter Availability: ")

                if fix_availability.lower() in ["yes","no"]:
                    self.availability = fix_availability
                    break

                else:
                    print("Respond with 'yes' or 'no'")
                    continue




# book1 = Book("Eggs", "suess", "123-456789-712345-67", "childrens", "08-12-1960", "maybe" )
# print(book1.availability)

# # print(book1.isbn)

# # book1.check_isbn()

# # print(book1.isbn)

# print(book1.publication_date)
