# Overview

{This project demonstrates a simple book management system that interacts with a SQL relational database. The purpose of this software is to enhance my understanding of SQL integration with Python while developing a practical, real-world application. The program allows users to manage books and authors, including adding, deleting, and viewing books, as well as updating the read count for each book.}

{This program uses a relational database to store information about books and their authors, showcasing CRUD (Create, Read, Update, Delete) operations and demonstrating a join query between two tables. It’s designed to improve my skills in database management and software development.}


[Software Demo Video](https://youtu.be/yzOV1iDlmNA)

# Relational Database

{The relational database used in this project consists of two tables:

1. Authors Table
- author_id: Unique identifier for each author (Primary Key).
- name: Name of the author (Unique).

2. Books Table
- title: Title of the book (Primary Key).
- pages: Number of pages in the book.
- read: Number of times the book has been read.
- author_id: Foreign key linking to the author_id in the authors table.

The database ensures data consistency through the use of a foreign key constraint, allowing each book to be associated with a valid author.}

# Development Environment

{
- SQLite: For creating and managing the database.
- Python 3: For writing the program and integrating with the database.
- VS Code: As the code editor.}

{sqlite3: Python library for interacting with SQLite databases.}

# Useful Websites

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3](https://docs.python.org/3.8/library/sqlite3.html)
- [TuotialsPoint: SQLite - Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

- Add a date_added column to the books table and implement filtering books by date.
- Improve error handling, such as handling invalid menu options or input errors gracefully.
- Retain database data between sessions by removing the table drop functionality.
- Create a graphical user interface (GUI) to make the program more user-friendly.
- Enhance querying features, such as searching for books or authors based on partial matches.