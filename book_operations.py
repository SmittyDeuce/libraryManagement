import re
from book_class import Book

# Initialize an empty library dictionary to store books
library = {}

# Function to add a book to the library
def add_book():
    while True:
        enter_title = input("Enter Title: *enter 'done' when finished* ")
        if enter_title.lower() == 'done':
            print(library)
            break

        enter_author = input("Enter author: ")
        enter_isbn = input("Enter ISBN: ")
        enter_genre = input("Enter genre: ")
        enter_publication_date = input("Enter publication date (MM-DD-YYYY): ")
        enter_availability = input("Enter availability (Yes/No): ")

        # Create a new Book instance
        library_book = Book(enter_title, enter_author, enter_isbn, enter_genre, enter_publication_date, enter_availability)
        if library_book.isbn not in library:
            # Add the book to the library dictionary if the ISBN is not already present
            library[library_book.isbn] = {
                "Title": library_book.title,
                "Author": library_book.author,
                "Genre": library_book.genre,
                "Publication Date": library_book.publication_date,
                "Availability": library_book.availability
            }
        else:
            print("This Book is already inside Library")



def borrow_book(users_dict):
    # Borrowing a book
    enter_title = input("Enter title to Borrow: *enter 'done' when finished* ")
    if enter_title.lower() == 'done':
        return
    for isbn, details in library.items():
        if enter_title.lower() == details["Title"].lower() and details["Availability"] == "yes":
            user_id = input("Enter your User ID: ")
            if user_id in users_dict:
                # Add the book to user's borrowed_books list
                users_dict[user_id]['borrowed_books'].append(enter_title)
                details["Availability"] = "no"
                print(f"{enter_title} has been checked out.")
                return
            else:
                print("User ID not found.")
                return
        elif enter_title.lower() == details["Title"].lower() and details["Availability"] == "no":
            print(f"{enter_title} is not available.")
            return
    print("Book is not in our library.")

def return_book(users_dict):
    while True:
        try:
            # Check if the library is empty
            if len(library) == 0:
                print("Library is empty")
                break

            # Prompt the user to enter the title of the book they want to return
            enter_title = input("Enter title to return book: *enter 'done' when finished* \n")
            if enter_title.lower() == 'done':
                break
            
            book_found = False
            for isbn, details in library.items():
                if enter_title.lower() == details["Title"].lower():  # Ensure case-insensitive comparison
                    book_found = True
                    if details["Availability"].lower() == "yes":
                        print(f"{enter_title} has already been returned.")
                        continue

                    elif details["Availability"].lower() == "no":
                        user_id = input("Enter your User ID: ")
                        if user_id in users_dict and enter_title in users_dict[user_id]['borrowed_books']:
                            print(f"{enter_title} has been returned.")
                            details["Availability"] = "yes"
                            users_dict[user_id]['borrowed_books'].remove(enter_title)
                        else:
                            print(f"{enter_title} is not borrowed by this user.")
                    break

            if not book_found:
                print("Book is not in our library.")

        except Exception as e:
            print("An error occurred:", e)

def search_book():
    
    while True:
        try:
            if len(library) == 0:
                print("library is empty")
                break

            search_by = input("Enter Title or ISBN to Search: *enter 'done' when finished\n")
            if search_by.lower() == 'done':
                break

            for isbn, details in library.items():
                if search_by == isbn or details["Title"].lower() == search_by.lower():
                    print(f"ISBN: {isbn}")
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    break

                else:
                    print("ISBN or Title not found, try again")
                    continue

        except Exception as e:
            print("An error has occured", e)

def display_books():
    while True:
        try:
            if len(library) == 0:
                print("library is empty")
                break

            for isbn, details in library.items():
                print(f"Title: {details['Title']}")
            break

        except Exception as e:
            print("An error has occured", e)


def book_operations(users_dict):
    while True:
        print("1. Add Book\n"
              "2. Borrow Book\n"
              "3. Return Book\n"
              "4. Search Book\n"
              "5. Display Books\n"
              "6. Quit")
        try:
            enter_option = int(input("Enter an Option: "))
            if enter_option == 6:
                break
            elif enter_option not in range(1, 7):
                print("Response must be between 1 and 6")
            elif enter_option == 1:
                add_book()
            elif enter_option == 2:
                borrow_book(users_dict)
            elif enter_option == 3:
                return_book(users_dict)
            elif enter_option == 4:
                search_book()
            elif enter_option == 5:
                display_books()
        except ValueError:
            print("Enter an integer between 1 and 6")

# add_book()
# # borrow_book()
# # return_book()
# search_book()
# display_books()

# book_operations()