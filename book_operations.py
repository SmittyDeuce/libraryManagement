import re
import mysql.connector
from main_database import connect_database, close_database
from book_class import Book

# Function to add a book to the library
def add_book():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    
    while True:
        # Prompt user to enter book details
        enter_title = input("Enter Title: *enter 'done' when finished* ")
        if enter_title.lower() == 'done':
            # If user inputs 'done', exit the loop
            break

        enter_author = input("Enter author: ")
        enter_isbn = input("Enter ISBN: ")
        enter_genre = input("Enter genre: ")
        enter_publication_date = input("Enter publication date (YYYY-MM-DD): ")
        enter_availability = input("Enter availability (Yes/No): ").lower()

        # Create a new Book instance
        library_book = Book(enter_title, enter_author, enter_isbn, enter_genre, enter_publication_date, enter_availability)

        try:
            # Insert the book details into the books table
            cursor.execute("""
                INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability)
                VALUES (%s, (SELECT id FROM authors WHERE name=%s), (SELECT id FROM genres WHERE name=%s), %s, %s, %s)
            """, (library_book.title, library_book.author, library_book.genre, library_book.isbn, library_book.publication_date, library_book.availability == 'yes'))
            
            conn.commit()  # Commit the transaction
            print(f"Book '{library_book.title}' added to the library.")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
    close_database(conn, cursor)  # Close the database connection

# Function to borrow a book from the library
def borrow_book(users_dict):
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    
    while True:
        enter_title = input("Enter title to Borrow: *enter 'done' when finished* ")
        if enter_title.lower() == 'done':
            break
        
        # Search for the book by title in the books table
        cursor.execute("SELECT id, availability FROM books WHERE title = %s", (enter_title,))
        book = cursor.fetchone()
        
        if book:
            book_id, availability = book
            if availability:
                user_id = input("Enter your User ID: ")
                if user_id in users_dict:
                    # Insert a record into borrowed_books table and update book availability
                    cursor.execute("""
                        INSERT INTO borrowed_books (user_id, book_id, borrow_date)
                        VALUES (%s, %s, CURDATE())
                    """, (user_id, book_id))
                    
                    cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
                    conn.commit()  # Commit the transaction
                    print(f"{enter_title} has been checked out.")
                else:
                    print("User ID not found.")
            else:
                print(f"{enter_title} is not available.")
        else:
            print("Book is not in our library.")
    
    close_database(conn, cursor)  # Close the database connection

# Function to return a borrowed book to the library
def return_book(users_dict):
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries

    while True:
        enter_title = input("Enter title to return book: *enter 'done' when finished* \n")
        if enter_title.lower() == 'done':
            break
        
        # Search for the book by title in the books table
        cursor.execute("SELECT id FROM books WHERE title = %s", (enter_title,))
        book = cursor.fetchone()

        if book:
            book_id = book[0]
            user_id = input("Enter your User ID: ")
            if user_id in users_dict:
                # Delete the record from borrowed_books table and update book availability
                cursor.execute("""
                    DELETE FROM borrowed_books
                    WHERE user_id = %s AND book_id = %s
                """, (user_id, book_id))
                
                cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
                conn.commit()  # Commit the transaction
                print(f"{enter_title} has been returned.")
            else:
                print(f"{enter_title} is not borrowed by this user.")
        else:
            print("Book is not in our library.")
    
    close_database(conn, cursor)  # Close the database connection

# Function to search for a book in the library
def search_book():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries

    while True:
        search_by = input("Enter Title or ISBN to Search: *enter 'done' when finished\n")
        if search_by.lower() == 'done':
            break
        
        # Search for the book by ISBN or title in the books table
        cursor.execute("SELECT * FROM books WHERE isbn = %s OR title = %s", (search_by, search_by))
        book = cursor.fetchone()

        if book:
            print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre ID: {book[3]}, ISBN: {book[4]}, Publication Date: {book[5]}, Availability: {'Yes' if book[6] else 'No'}")
        else:
            print("Book not found.")
    
    close_database(conn, cursor)  # Close the database connection

# Function to display the titles of all books in the library
def display_books():
    conn = connect_database()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries

    # Select all book titles from the books table
    cursor.execute("SELECT title FROM books")
    books = cursor.fetchall()

    if books:
        for book in books:
            print(f"Title: {book[0]}")
    else:
        print("Library is empty.")
    
    close_database(conn, cursor)  # Close the database connection

# Function to handle book-related operations
def book_operations(users_dict):
    while True:
        print("1. Add Book\n"
              "2. Borrow Book\n"
              "3. Return Book\n"
              "4. Search Book\n"
              "5. Display Books\n"
              "6. Quit")
        try:
            enter_option = int(input("Enter an Option: "))
            if enter_option == 6:
                break
            elif enter_option not in range(1, 7):
                print("Response must be between 1 and 6")
            elif enter_option == 1:
                add_book()  # Call function to add a book
            elif enter_option == 2:
                borrow_book(users_dict)  # Call function to borrow a book
            elif enter_option == 3:
                return_book(users_dict)  # Call function to return a book
            elif enter_option == 4:
                search_book()  # Call function to search for a book
            elif enter_option == 5:
                display_books()  # Call function to display all books
        except ValueError:
            print("Enter an integer between 1 and 6")