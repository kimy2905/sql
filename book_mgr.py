import sqlite3

# 1 Connect to the database
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# 2 Create tables
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS authors")

# 2 Create authors table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
""")

# 2 Create books table with author_id as a foreign key
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        title TEXT PRIMARY KEY,
        pages INTEGER,
        read INTEGER,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors (author_id)
    )
""")

# 3 Helper function to get or insert an author
def get_or_create_author(author_name):
    cursor.execute("SELECT author_id FROM authors WHERE name = ?", (author_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
    connection.commit()
    return cursor.lastrowid

choice = None
while choice != 6:
    print("\nSelect an option:")
    print("1) Add a new book")
    print("2) Delete a book")
    print("3) Show all books")
    print("4) Read a book")
    print("5) Show books with authors")
    print("6) Exit")
    choice = int(input("> "))

# 4 Adding a new book 
    if choice == 1:
        title = input("Enter book name: ")
        pages = int(input("Enter number of pages: "))
        author_name = input("Enter author's name: ")
        read = 0

        # Get or create the author and retrieve their ID
        author_id = get_or_create_author(author_name)
        try:
            cursor.execute(
                "INSERT INTO books (title, pages, read, author_id) VALUES (?, ?, ?, ?)",
                (title, pages, read, author_id)
            )
            connection.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Book with this title already exists.")
    #7 Deleting a book
    elif choice == 2:
        title = input("Enter the book to remove: ")
        cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        connection.commit()
        if cursor.rowcount == 0:
            print("ERROR! Book does not exist.")
        else:
            print("Book removed successfully.")

    elif choice == 3:
    # 5 Viewing books
        cursor.execute("SELECT * FROM books ORDER BY title")
        print("\nBooks:")
        for record in cursor.fetchall():
            print(f"Title: {record[0]}, Pages: {record[1]}, Read: {record[2]}")
    
    elif choice == 4:
    # 6 reading a book
        cursor.execute("SELECT title, read FROM books ORDER BY title")
        records = cursor.fetchall()
        for index, record in enumerate(records, start=1):
            print(f"{index}) {record[0]} (Read {record[1]} times)")
        choice = int(input("> "))
        selected_title = records[choice - 1][0]
        cursor.execute("UPDATE books SET read = read + 1 WHERE title = ?", (selected_title,))
        connection.commit()
        print("Book read count updated.")

# 5 authors
    elif choice == 5:
        cursor.execute("""
            SELECT books.title, books.pages, books.read, authors.name
            FROM books
            JOIN authors ON books.author_id = authors.author_id
            ORDER BY books.title
        """)
        print("\nBooks with Authors:")
        for record in cursor.fetchall():
            print(f"Title: {record[0]}, Pages: {record[1]}, Read: {record[2]}, Author: {record[3]}")

# 8 Closing the program
print("Goodbye!")
connection.close()

