from author_class import Author
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

# Function to add an author to the dictionary
def add_author():
    while True:
        try:
            # Prompt user to enter author details
            enter_name = input("Enter author name: *enter 'done' when finished ")

            if enter_name.lower() == 'done':
                print(authors_dict)
                break
            if enter_name in authors_dict:
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

# Function to display author details
def author_details():
    while True:
        enter_name = input("Enter Name: *enter 'done' when finished\n")

        if enter_name.lower() == 'done':
            break

        for name, details in authors_dict.items():
            if enter_name.lower() == name.lower():
                print("")
                print(f"Name: {enter_name}")
                for key, value in details.items():
                    print(f"{key}: {value}")
                break
        else:
            print("Author is not in our directory")
            continue

# Function to display all authors
def display_authors():
    while True:
        try:
            for author in authors_dict:
                print("")
                print(f"Author Name:{author}")
            break

        except Exception as e:
            print("An error has occurred", e)

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
                if len(authors_dict) == 0:
                    print("Authors directory is empty")
                    continue
                else:
                    author_details()

            elif enter_option == 3:
                if len(authors_dict) == 0:
                    print("Authors directory is empty")
                    continue
                else:
                    display_authors()

        except ValueError:
            print("Enter an integer between 1 and 4")


# # author_details()
# add_author()
# # author_details()
# display_authors()

# author_operations()