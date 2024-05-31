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
                enter_title = input("Enter Title: ")
                counter += 1
                # "book" + counter
                

            elif menu_option == 2:
                pass

            elif menu_option == 3:
                pass

            elif menu_option == 4:
                pass

        except ValueError:
            print("Menu Option must be number 1 - 5")
            continue
book_Operations()