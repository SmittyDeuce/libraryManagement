from user_class import User

users_dict = {}
def add_users():
    while True:
        try:
            enter_id = input("Enter an ID (7) digits:*enter 'done' when finished\n")
            
            if enter_id.lower() == 'done':
                for user in users_dict.items():
                    print(f"Users: {user[0]} added")
                break


            elif enter_id not in users_dict:
                enter_name = input("Enter Name: *enter 'done' when finished\n")

                user = User(enter_name, enter_id)
                users_dict[enter_id] = {
                    "user_name":enter_name,
                    "borrowed_books":user.borrowed_books
                }

            else:
                print("User with ID Exists")
                continue

        except Exception as e:
            print("names must be 2 letters or more\nid must be 7 digits")
            continue

def user_details():
    while True:
        try:
            if len(users_dict) == 0:
                print("User list is empty")
                break

            enter_id = input("Enter an ID (7) digits:*enter 'done' when finished\n")
            
            if enter_id.lower() == 'done':
                break
            
            found = False
            for user_id, details in users_dict.items():
                if enter_id == user_id:
                    print(f"User ID: {user_id}")
                    for key, value in details.items():
                        print(f"{key}, {value}")
                    found = True
                    break
            
            if not found:
                print("User ID not found")
                
        except Exception as e:
            print("ID must be 7 digits")
            continue

def display_users():
    if len(users_dict) == 0:
            print("User list is empty")

    for user_id, details in users_dict.items():
        print(f"User ID: {user_id}\nUserName: {details['user_name']}")
            
def user_operations():
    while True:
        try:
            print("1. Add User\n"
                  "2. User Details\n"
                  "3. Display Users\n"
                  "4. Quit")
            
            enter_option = int(input("Enter an Option: "))
            if enter_option == 4:
                break
            
            elif enter_option not in range(1, 5):
                print("Response must be between 1 and 4")

            elif enter_option == 1:
                add_users()
            elif enter_option == 2:
                user_details()
            elif enter_option == 3:
                display_users()

        except ValueError:
            print("Enter an integer between 1 and 4")

# display_users()
# add_users()
# display_users()

