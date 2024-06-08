from book_operations import book_operations
# from user_operations import user_operations




print("Welcome to the Library Management System!\n"
      "Main Menu:")
print("1. Book Operations\n"
      "2. User Operations\n"
      "3. Author Operations\n"
      "4. Genre Operations\n"
      "5. Quit"
)

def management_system():
    while True:
        try:
            enter_option = int(input("Enter an Option: "))

            if enter_option == 5:
                break
            
            elif enter_option == 1:
               book_operations()

            elif enter_option == 2:
                # user_operations()
        
            elif enter_option == 3:
               pass
        
            elif enter_option == 4:
                pass



        except Exception as e:
            print("An error occured", e)
            continue

        except ValueError("Enter a number between 1 and 5"):
            continue


# management_system()