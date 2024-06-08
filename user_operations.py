from user_class import User  # Importing the User class from the user_class module

users_dict = {}  # Dictionary to store user information

def add_users():
    """Function to add users to the library system."""
    while True:
        try:
            enter_id = input("Enter an ID (7 digits): *enter 'done' when finished\n")
            
            if enter_id.lower() == 'done':
                # Print the list of added users and exit the loop when 'done' is entered
                for user in users_dict.items():
                    print(f"Users: {user[0]} added")
                break

            elif enter_id not in users_dict:
                # If the entered ID is not in the dictionary, prompt for user details and add to dictionary
                enter_name = input("Enter Name: *enter 'done' when finished\n")

                user = User(enter_name, enter_id)
                # Add user details to the users_dict dictionary
                users_dict[enter_id] = {
                    "user name": enter_name,
                    "borrowed books": user.borrowed_books
                }

            else:
                # If the ID already exists in the dictionary, inform the user
                print("User with ID already exists")
                continue

        except Exception as e:
            # Catch any exceptions (e.g., invalid input) and inform the user
            print("Names must be 2 letters or more\nID must be 7 digits")
            continue

def user_details():
    """Function to display details of a specific user."""
    while True:
        try:
            if len(users_dict) == 0:
                # If the user dictionary is empty, inform the user and exit the loop
                print("User list is empty")
                break

            enter_id = input("Enter an ID (7 digits): *enter 'done' when finished\n")
            
            if enter_id.lower() == 'done':
                # If 'done' is entered, exit the loop
                break
            
            found = False
            for user_id, details in users_dict.items():
                if enter_id == user_id:
                    # If the entered ID matches an ID in the dictionary, display user details
                    print("")
                    print(f"User ID: {user_id}")
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    found = True
                    break
            
            if not found:
                # If the entered ID is not found in the dictionary, inform the user
                print("User ID not found")
                
        except Exception as e:
            # Catch any exceptions (e.g., invalid input) and inform the user
            print("ID must be 7 digits")
            continue

def display_users():
    """Function to display all users in the system."""
    if len(users_dict) == 0:
        # If the user dictionary is empty, inform the user
        print("User list is empty")

    for user_id, details in users_dict.items():
        # Iterate through the user dictionary and display user IDs and names
        print(f"User ID: {user_id}\nUser Name: {details['user name']}")
            
def user_operations():
    """Function to manage user operations."""
    while True:
        try:
            print("1. Add User\n"
                  "2. User Details\n"
                  "3. Display Users\n"
                  "4. Quit")
            
            enter_option = int(input("Enter an Option: "))
            if enter_option == 4:
                # If '4' is entered, exit the loop and quit the program
                break
            
            elif enter_option not in range(1, 5):
                # If an invalid option is entered, inform the user
                print("Response must be between 1 and 4")

            elif enter_option == 1:
                # If '1' is entered, call the add_users() function to add a user
                add_users()
            elif enter_option == 2:
                # If '2' is entered, call the user_details() function to display user details
                user_details()
            elif enter_option == 3:
                # If '3' is entered, call the display_users() function to display all users
                display_users()

        except ValueError:
            # Catch any exceptions (e.g., invalid input) and inform the user
            print("Enter an integer between 1 and 4")