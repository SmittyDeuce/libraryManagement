from genre_class import Genre  # Importing the Genre class from the genre_class module

genres_dict = {}  # Dictionary to store genre information

def add_genre():
    """Function to add a genre to the library system."""
    while True:
        try:
            enter_name = input("Enter genre name: *enter 'done' when finished ")

            if enter_name.lower() == 'done':
                # If 'done' is entered, print the genres dictionary and exit the loop
                print(genres_dict)
                break
            if enter_name in genres_dict:
                # If the entered genre name is already in the dictionary, inform the user
                print("Genre is already listed")
                continue

            enter_description = input("Enter description: ")
            enter_category = input("Enter category: ")

            genre = Genre(enter_name, enter_description, enter_category)

            if enter_name not in genres_dict:
                # If the genre name is not already in the dictionary, add it along with its details
                genres_dict[genre.name] = {
                    "Description": genre.description,
                    "Category": genre.category
                }
                print(f"Genre {enter_name} added.")

        except Exception as e:
            # Catch any exceptions (e.g., invalid input) and inform the user
            print("An error occurred:", e)

def genre_details():
    """Function to display details of a specific genre."""
    while True:
        enter_name = input("Enter Genre Name: *enter 'done' when finished\n")

        if enter_name.lower() == 'done':
            # If 'done' is entered, exit the loop
            break

        if enter_name in genres_dict:
            # If the entered genre name is found in the dictionary, display its details
            print("")
            print(f"Name: {enter_name}")
            for key, value in genres_dict[enter_name].items():
                print(f"{key.capitalize()}: {value}")
        else:
            # If the entered genre name is not found in the dictionary, inform the user
            print("Genre is not in our directory")

def display_genres():
    """Function to display all genres in the system."""
    if len(genres_dict) == 0:
        # If the genre dictionary is empty, inform the user
        print("Genres directory is empty")
    else:
        # Otherwise, iterate through the dictionary and display all genre names
        for genre in genres_dict:
            print(f"Genre Name: {genre}")

def genre_operations(genres_dict):
    """Function to manage genre operations."""
    while True:
        print("1. Add Genre\n"
              "2. View Genre Details\n"
              "3. Display All Genres\n"
              "4. Quit")
        try:
            enter_option = int(input("Enter an Option: "))

            if enter_option == 4:
                # If '4' is entered, exit the loop and quit the program
                break

            elif enter_option not in range(1, 5):
                # If an invalid option is entered, inform the user
                print("Response must be between 1 and 4")

            elif enter_option == 1:
                # If '1' is entered, call the add_genre() function to add a genre
                add_genre()

            elif enter_option == 2:
                # If '2' is entered, call the genre_details() function to display genre details
                if len(genres_dict) == 0:
                    print("Authors directory is empty")
                    continue
                else:
                    genre_details()

            elif enter_option == 3:
                # If '3' is entered, call the display_genres() function to display all genres
                if len(genres_dict) == 0:
                    print("Authors directory is empty")
                    continue
                else:
                    display_genres()

        except ValueError:
            # Catch any exceptions (e.g., invalid input) and inform the user
            print("Enter an integer between 1 and 4")