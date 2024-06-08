# Library Management System

Welcome to the Library Management System! This system allows you to perform various operations related to managing books, users, authors, and genres in a library.

## Main Menu

1. **Book Operations**
2. **User Operations**
3. **Author Operations**
4. **Genre Operations**
5. **Quit**

## How to Use

1. **Book Operations**
    - This option allows you to perform operations related to books in the library.
    - test ISBN to copy for book operations: `123-456789-712345-67`
    
2. **User Operations**
    - Perform operations related to library users.

3. **Author Operations**
    - Perform operations related to authors and their details.

4. **Genre Operations**
    - Perform operations related to book genres.

## Usage Instructions

1. Run the `main.py` file to start the Library Management System.
2. Select an option from the main menu by entering the corresponding number.
3. Follow the prompts to perform the desired operation.
4. Use the provided ISBN for book operations to test functionalities related to adding, borrowing, returning, and searching for books.

## Requirements

- Required Python modules: `book_operations`, `user_operations`, `author_operations`, `genre_operations`


# Book Class

The `Book` class represents a book in the library management system. It contains attributes such as title, author, ISBN, genre, publication date, and availability.

## Attributes

- **Title**: The title of the book.
- **Author**: The author of the book.
- **ISBN**: The International Standard Book Number of the book.
- **Genre**: The genre of the book.
- **Publication Date**: The date when the book was published.
- **Availability**: Indicates whether the book is available for borrowing or not.

### Validation

- **Publication Date:** Validates the format of the publication date (MM-DD-YYYY). If the format is incorrect, it prompts the user for a valid date.

- **ISBN:** Validates the format of the ISBN using regular expressions. If the format is incorrect, it prompts the user for a valid ISBN.

- **Availability:** Validates the availability status. If the input is not 'Yes' or 'No', it prompts the user for a valid availability status.

### Book Operations

The `book_operations` module provides functionality for managing books in the library.

#### Functions

1. **Add Book**
   - Allows users to add a new book to the library.
   - Prompts the user to enter details such as title, author, ISBN, genre, publication date, and availability.
   - Validates the publication date format (MM-DD-YYYY), ISBN format using regular expressions, and availability status.
   - If the input formats are incorrect, it prompts the user for valid input.

2. **Borrow Book**
   - Enables users to borrow a book from the library.
   - Prompts the user to enter the title of the book they want to borrow.
   - Validates the availability status of the book. If the book is available, it checks if the user exists and adds the book to the user's borrowed books list.
   - If the book is not available or the user does not exist, appropriate error messages are displayed.

3. **Return Book**
   - Allows users to return a borrowed book to the library.
   - Prompts the user to enter the title of the book they want to return.
   - Validates if the book exists in the library and if it has been borrowed by the user.
   - If the book is found and has been borrowed by the user, it updates the availability status and removes the book from the user's borrowed books list.

4. **Search Book**
   - Enables users to search for a book in the library by title or ISBN.
   - Prompts the user to enter the title or ISBN of the book they want to search.
   - Displays the details of the book if found, including ISBN, title, author, genre, publication date, and availability.

5. **Display Books**
   - Displays the titles of all books available in the library.

6. **Quit**
   - Exits the book operations menu.


# User Class

## Overview
The User Class represents a library user in the Library Management System. It includes functionalities for creating users, validating user information, and managing borrowed books.

## Features
- Create a new user with a name and ID.
- Validate user information:
  - Name: Must be at least two letters long for both first and last names.
  - ID: Must be exactly 7 digits long.
- Maintain a list of borrowed books for each user.

## Usage Instructions
1. To create a new user, enter the user's name and ID.
2. Follow the prompts to input valid user information.
3. The system will validate the user's name and ID according to the specified criteria.
4. Once created, the user's information will be stored in the system, along with their list of borrowed books.


# User Operations

## Overview
User Operations allow administrators to manage users within the Library Management System. These operations include adding new users, viewing user details, and displaying a list of all users.

## Features
- Add new users to the system.
- View details of existing users, including their name, ID, and borrowed books.
- Display a list of all users in the system.

## Usage Instructions
1. Select the "User Operations" option from the main menu.
2. Choose an operation from the available options:
   - **Add User**: Enter user details to create a new user.
   - **User Details**: View details of an existing user by entering their ID.
   - **Display Users**: View a list of all users currently registered in the system.
3. Follow the prompts to perform the desired operation.
4. Ensure that user information, such as name and ID, meets the specified criteria for validation.

# Author Class

## Overview
The Author class represents authors and their details within the Library Management System. It allows for the creation of author objects with attributes such as name, age, birth city, and zodiac sign.

## Attributes
- **Name**: The name of the author.
- **Age**: The age of the author.
- **Origin Place**: The birth city or place of origin of the author.
- **Zodiac**: The zodiac sign of the author.

# Author Operations

## Overview
Author Operations allow administrators to manage authors and their details within the Library Management System. These operations include adding new authors, viewing author details, and displaying a list of all authors.

## Features
- Add new authors to the system with their name, age, birth city, and zodiac sign.
- View details of existing authors, including their name, age, birth city, and zodiac sign.
- Display a list of all authors currently registered in the system.

## Usage Instructions
1. Select the "Author Operations" option from the main menu.
2. Choose an operation from the available options:
   - **Add Author**: Enter author details to add a new author to the system.
   - **View Author Details**: Enter the name of the author to view their details.
   - **Display All Authors**: View a list of all authors currently registered in the system.
3. Follow the prompts to perform the desired operation.
4. Ensure that author information, such as name, age, and zodiac sign, is entered accurately.

# Genre Class

## Overview
The Genre class represents different book genres within the Library Management System. It allows for the creation of genre objects with attributes such as name, description, and category.

## Attributes
- **Name**: The name of the genre.
- **Description**: A brief description or summary of the genre.
- **Category**: The category or classification of the genre (e.g., fiction, non-fiction, mystery, romance, etc.).

# Genre Operations

## Overview
Genre Operations allow users to perform various tasks related to book genres within the Library Management System. These operations include adding new genres, viewing genre details, and displaying all genres available in the system.

## Available Operations

1. **Add Genre**: Allows users to add a new genre to the system by providing the name, description, and category of the genre.
2. **View Genre Details**: Enables users to view the details of a specific genre, including its name, description, and category.
3. **Display All Genres**: Displays a list of all genres available in the system.

## Usage Instructions
1. Run the Library Management System.
2. Select "Genre Operations" from the main menu.
3. Choose the desired operation by entering the corresponding number.
4. Follow the prompts to perform the selected operation.

### Add Genre
- Enter the name, description, and category of the new genre when prompted.
- Ensure that the provided information is accurate and descriptive.

### View Genre Details
- Enter the name of the genre you want to view details for.
- The system will display the name, description, and category of the selected genre.

### Display All Genres
- This option displays a list of all genres available in the system.
- It provides an overview of the genres currently stored in the system.