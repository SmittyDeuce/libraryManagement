from genre_class import Genre  # Importing the Genre class from the genre_class module
from main_database import connect_database, close_database  # Import database connection functions

# Initialize an empty dictionary to store genre information
genres_dict = {}

# Function to add a genre to the database
def add_genre():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        try:
            # Prompt user to enter genre details
            enter_name = input("Enter genre name: *enter 'done' when finished ")

            if enter_name.lower() == 'done':
                # Print the genres dictionary and exit the loop when 'done' is entered
                print(genres_dict)
                break
            if enter_name in genres_dict:
                # Check if the genre is already listed
                print("Genre is already listed")
                continue

            enter_description = input("Enter description: ")
            enter_category = input("Enter category: ")

            # Create Genre object and add to dictionary
            genre = Genre(enter_name, enter_description, enter_category)
            if enter_name not in genres_dict:
                # Insert genre details into the database
                cursor.execute("""
                    INSERT INTO genres (name, description, category)
                    VALUES (%s, %s, %s)
                """, (enter_name, enter_description, enter_category))
                conn.commit()

                genres_dict[genre.name] = {
                    "Description": genre.description,
                    "Category": genre.category
                }
                print(f"Genre {enter_name} added.")

        except Exception as e:
            print("An error occurred:", e)
    
    close_database(conn, cursor)  # Close the database connection

# Function to display genre details
def genre_details():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        enter_name = input("Enter Genre Name: *enter 'done' when finished\n")

        if enter_name.lower() == 'done':
            break

        cursor.execute("SELECT * FROM genres WHERE name = %s", (enter_name,))
        result = cursor.fetchone()
        if result:
            print("")
            print(f"Name: {result[1]}")
            print(f"Description: {result[2]}")
            print(f"Category: {result[3]}")
        else:
            print("Genre is not in our directory")
    
    close_database(conn, cursor)  # Close the database connection

# Function to display all genres
def display_genres():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        try:
            cursor.execute("SELECT name FROM genres")
            results = cursor.fetchall()
            for result in results:
                print(f"Genre Name: {result[0]}")
            break

        except Exception as e:
            print("An error has occurred", e)
    
    close_database(conn, cursor)  # Close the database connection

# Function to manage genre operations
def genre_operations(genres_dict):
    while True:
        print("1. Add Genre\n"
              "2. View Genre Details\n"
              "3. Display All Genres\n"
              "4. Quit")
        try:
            enter_option = int(input("Enter an Option: "))

            if enter_option == 4:
                break

            elif enter_option not in range(1, 5):
                print("Response must be between 1 and 4")

            elif enter_option == 1:
                add_genre()

            elif enter_option == 2:
                genre_details()

            elif enter_option == 3:
                display_genres()

        except ValueError:
            print("Enter an integer between 1 and 4")
