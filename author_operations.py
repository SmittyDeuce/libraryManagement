from author_class import Author  # Import Author class from author_class module
from main_database import connect_database, close_database  # Import database connection functions

# Initialize an empty dictionary to store author information
authors_dict = {}
zodiac_signs = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]

# Function to add an author to the database
def add_author():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        try:
            # Prompt user to enter author details
            enter_name = input("Enter author name: *enter 'done' when finished ")

            if enter_name.lower() == 'done':
                # Print the authors dictionary and exit the loop when 'done' is entered
                print(authors_dict)
                break
            if enter_name in authors_dict:
                # Check if the author is already listed
                print("Author is already listed")
                continue

            enter_age = int(input("Enter age: "))
            enter_city = input("Enter birth city: ")
            enter_zodiac = input("Enter Zodiac: ")

            # Validate entered Zodiac sign
            if enter_zodiac.lower() not in [sign.lower() for sign in zodiac_signs]:
                print("Invalid response, check spelling.")
                continue
            
            # Create Author object and add to dictionary
            author = Author(enter_name, enter_age, enter_city, enter_zodiac)
            if enter_name not in authors_dict:
                # Insert author details into the database
                cursor.execute("""
                    INSERT INTO authors (name, age, birth_city, zodiac_sign)
                    VALUES (%s, %s, %s, %s)
                """, (enter_name, enter_age, enter_city, enter_zodiac))
                conn.commit()

                authors_dict[author.name] = {
                    "Zodiac": author.zodiac,
                    "Age": author.age,
                    "City": author.origin_place
                }
                print(f"Author {enter_name} added.")

        except ValueError:
            print("Age must be an integer")
            continue
        except Exception as e:
            print("An error occurred:", e)
    
    close_database(conn, cursor)  # Close the database connection

# Function to display author details
def author_details():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        enter_name = input("Enter Name: *enter 'done' when finished\n")

        if enter_name.lower() == 'done':
            break

        cursor.execute("SELECT * FROM authors WHERE name = %s", (enter_name,))
        result = cursor.fetchone()
        if result:
            print("")
            print(f"Name: {result[1]}")
            print(f"Age: {result[2]}")
            print(f"Birth City: {result[3]}")
            print(f"Zodiac Sign: {result[4]}")
        else:
            print("Author is not in our directory")
            continue
    
    close_database(conn, cursor)  # Close the database connection

# Function to display all authors
def display_authors():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()

    while True:
        try:
            cursor.execute("SELECT name FROM authors")
            results = cursor.fetchall()
            for result in results:
                print("")
                print(f"Author Name: {result[0]}")
            break

        except Exception as e:
            print("An error has occurred", e)
    
    close_database(conn, cursor)  # Close the database connection

# Function to manage author operations
def author_operations(authors_dict):
    while True:
        print("1. Add Author\n"
              "2. View Author Details\n"
              "3. Display All Authors\n"
              "4. Quit")
        try:
            enter_option = int(input("Enter an Option: "))

            if enter_option == 4:
                break

            elif enter_option not in range(1, 5):
                print("Response must be between 1 and 4")

            elif enter_option == 1:
                add_author()

            elif enter_option == 2:
                author_details()

            elif enter_option == 3:
                display_authors()

        except ValueError:
            print("Enter an integer between 1 and 4")
