from book_class import Book
library = {}

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

        library_book = Book(enter_title, enter_author, enter_isbn, enter_genre, enter_publication_date, enter_availability)
        if library_book.isbn not in library:
            library[library_book.isbn] = {
                "Title": library_book.title,
                "Author": library_book.author,
                "Genre": library_book.genre,
                "Publication Date": library_book.publication_date,
                "Availability": library_book.availability
            }
        else:
            print("This Book is already inside Library")

def borrow_book():
    while True:
        try:
            enter_title = input("Enter title to borrow book: *enter 'done' when finsished: ")
            if enter_title.lower() == 'done':
                break
            
            for isbn, details in library.items():
                if enter_title.lower() == details["Title"].lower():
                    if details["Availability"].lower() == "no":
                        print(f"{enter_title} is currently checked out")
                    
                    elif details["Availability"].lower() == 'yes':
                        details["Availability"] = "no"
                        print(f"{enter_title} has been checked out\n")
                        print(f"Availability: {details['Availability']}")
                    break
            else:
                print(f"{enter_title} not in Library")
                continue
        except Exception as e:
            print("An error has occured", e)
            continue

def return_book():
    while True:
        try:
            enter_title = input("Enter book title to return: *enter 'done' when finished\n")
            if enter_title.lower() == 'done':
                break
            for isbn, details in library.items():
                if enter_title not in details["Title"]:
                    print("Book doesn't belong to this library")
                    continue
                elif enter_title.lower() == details["Title"].lower() and details["Availability"].lower() == 'no':
                    print(f"Title: {details['Title']} Availability: {details['Availability']}")
                    details["Availability"] = 'yes'
                    print(f"Book returned\nTitle: {details['Title']} Availability: {details['Availability']}")
                    continue
                elif enter_title.lower() == details["Title"].lower() and details["Availability"].lower() == 'yes':
                    print("Book has already been returned")
                    continue
                else:
                    print("An Unexpected error occured: try again")
                    continue

        except Exception as e:
            print("An error has occured", e)
            continue


def search_for_book():
    while True:
        try:
            isbn_or_title = input("Enter ISBN or Title: *enter 'done' when finished ")

            if isbn_or_title.lower() == 'done':
                break

            for isbn, details in library.items():
                if isbn == isbn_or_title or details["Title"].lower() == isbn_or_title.lower():
                    print(f"ISBN: {isbn}")
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    break

                else:
                    print("ISBN or Title not found try again")
                    continue


        except Exception as e:
            print("An error has occured", e)
            continue

def display_library():
    for isbn, details in library.items():
        print(f"ISBN: {isbn}")
        for key, value in details.items():
            print(f"{key}: {value}")
        break







def book_Operations():
    print("1. Add Book\n"
          "2. Borrow Book\n"
          "3. Return Book\n"
          "4. Search for Book\n"
          "5. Display Library\n"
          "6. Quit")
    
    while True:
        try:
            menu_option = int(input("Enter Option: "))
            if menu_option == 6:
                break
            
            elif menu_option not in range(1,6):
                print("Please enter one of the options")
                continue

            elif menu_option == 1:
                add_book()

            elif menu_option == 2:
                if len(library) <= 0:
                    print("Library is empty")
                    continue

                elif len(library) > 0:
                    borrow_book()
                                    
            elif menu_option == 3:
                if len(library) <= 0:
                    print("Library is empty")
                    continue

                elif len(library) > 0:
                    return_book()

            elif menu_option == 4:
                if len(library) <= 0:
                    print("Library is empty")
                    continue

                elif len(library) > 0:
                    search_for_book()

            elif menu_option == 5:
                if len(library) <= 0:
                    print("Library is empty")
                    continue

                else:
                    display_library()

        except ValueError:
            print("Menu Option must be number 1 - 6")
            continue


book_Operations()