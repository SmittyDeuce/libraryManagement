from book_class import Book
def book_Operations():

    library = {}
    counter = 0
    print("1. Add Book\n"
          "2. Borrow Book\n"
          "3. Return Book\n"
          "4. Search for Book\n"
          "5. Quit")
    
    while True:
        try:
            menu_option = int(input("Enter Option: "))


            if menu_option == 5:
                break
            
            elif menu_option not in range(1,5):
                print("Please enter one of the options")
                continue


            elif menu_option == 1:
                while True:

                    enter_title = input("Enter Title: *enter 'done' when finished* ")

                    if enter_title.lower() == 'done':
                        print(library)
                        break

                    counter += 1
                    enter_author = input("Enter author: ")
                    enter_isbn = input("Enter ISBN: ")
                    enter_genre = input("Enter genre: ")
                    enter_publication_date = input("Enter publication date (MM-DD-YYYY): ")
                    enter_availability = input("Enter availability (Yes/No): ")

                    library_book = counter
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
                

            elif menu_option == 2:
                if len(library) <= 0:
                    print("CAN'T BORROW ANY BOOK LIBRARY DOESN'T EXIST")
                    continue

                elif len(library) > 0:
                    
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
                                    


                        
            elif menu_option == 3:
                if len(library) <= 0:
                    print("CAN'T RETURN ANY BOOK LIBRARY DOESN'T EXIST")
                    continue

                elif len(library) > 0:
                    while True:
                        try:
                            enter_title = input("Enter Title of boo")

                        except Exception as e:
                            print("An error has occured", e)

            elif menu_option == 4:
                pass

        except ValueError:
            print("Menu Option must be number 1 - 5")
            continue
book_Operations()