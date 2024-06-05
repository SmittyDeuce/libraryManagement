from book_class import Book

library = {}

def add_book(title, author, isbn, genre, publication_date, availability):
    if isbn not in library:
        new_book = Book(title, author, isbn, genre, publication_date, availability)
        library[isbn] = {
            "Title": new_book.title,
            "Author": new_book.author,
            "Genre": new_book.genre,
            "Publication Date": new_book.publication_date,
            "Availability": new_book.availability
        }
        print(f"Book '{title}' added to the library.")
    else:
        print("This Book is already in the library.")

def borrow_book(title):
    for isbn, details in library.items():
        if title.lower() == details["Title"].lower():
            if details["Availability"].lower() == "no":
                print(f"{title} is currently checked out")
                return None
            elif details["Availability"].lower() == 'yes':
                details["Availability"] = "no"
                print(f"{title} has been checked out\n")
                return details
    print(f"{title} not in Library")
    return None

def return_book(title):
    for isbn, details in library.items():
        if title.lower() == details["Title"].lower():
            if details["Availability"].lower() == 'no':
                details["Availability"] = 'yes'
                print(f"Book returned\nTitle: {details['Title']} Availability: {details['Availability']}")
                return details
            else:
                print("Book has already been returned")
                return None
    print("Book not found in the library")
    return None

def display_library():
    if len(library) <= 0:
        print("Library is empty")
    else:
        for isbn, details in library.items():
            print(f"ISBN: {isbn}")
            for key, value in details.items():
                print(f"{key}: {value}")

def search_for_book(isbn_or_title):
    if len(library) <= 0:
        print("Library is empty")
        return None
    for isbn, details in library.items():
        if isbn == isbn_or_title or details["Title"].lower() == isbn_or_title.lower():
            return {isbn: details}
    print("Book not found")
    return None