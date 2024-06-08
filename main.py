from book_operations import book_operations, library
from user_operations import user_operations, users_dict
from author_operations import author_operations, authors_dict
from genre_operations import genre_operations, genres_dict
# ISBN to copy for  book operations: 123-456789-712345-67


def management_system():
    print("Welcome to the Library Management System!\n"
        "Main Menu:")
    
    while True:

        print("1. Book Operations\n"
      "2. User Operations\n"
      "3. Author Operations\n"
      "4. Genre Operations\n"
      "5. Quit"
)

        try:
            enter_option = int(input("Enter an Option: "))

            if enter_option == 5:
                break
            
            elif enter_option == 1:
               book_operations(users_dict)

            elif enter_option == 2:
                user_operations()
        
            elif enter_option == 3:
               author_operations(authors_dict)
        
            elif enter_option == 4:
                genre_operations(genres_dict)

        except ValueError as e:
            print("Enter a number between 1 and 5")
            continue


management_system()