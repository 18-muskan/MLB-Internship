import json


# Parent Class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def show_details(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} - {self.author} - {status}")


# Child Class
class EBook(Book):
    def __init__(self, title, author, file_size, available=True):
        super().__init__(title, author, available)
        self.file_size = file_size

    # Method Overriding
    def show_details(self):
        status = "Available" if self.available else "Borrowed"
        print(
            f"{self.title} - {self.author} - "
            f"EBook - {self.file_size} MB - {status}"
        )


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    # Add Book
    def add_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            if title == "" or author == "":
                print("Title and author cannot be empty.")
                return

            print("\n1. Normal Book")
            print("2. EBook")

            book_type = int(input("Enter book type: "))

            if book_type == 1:
                book = Book(title, author)

            elif book_type == 2:
                file_size = float(input("Enter file size in MB: "))
                book = EBook(title, author, file_size)

            else:
                print("Invalid book type.")
                return

            self.books.append(book)
            self.save_books()

            print("Book added successfully!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n===== All Books =====")

        for number, book in enumerate(self.books, start=1):
            print(number, end=". ")
            book.show_details()

    # Search Book
    def search_book(self):
        title = input("Enter book title to search: ")

        found = False

        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                book.show_details()
                found = True
                break

        if not found:
            print("Book not found.")

    # Borrow Book
    def borrow_book(self):
        title = input("Enter book title to borrow: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    self.save_books()

                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")

                return

        print("Book not found.")

    # Return Book
    def return_book(self):
        title = input("Enter book title to return: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.available:
                    book.available = True
                    self.save_books()

                    print("Book returned successfully!")
                else:
                    print("Book is already available.")

                return

        print("Book not found.")

    # Save Books to JSON
    def save_books(self):
        data = []

        for book in self.books:

            if isinstance(book, EBook):
                data.append({
                    "type": "ebook",
                    "title": book.title,
                    "author": book.author,
                    "file_size": book.file_size,
                    "available": book.available
                })

            else:
                data.append({
                    "type": "book",
                    "title": book.title,
                    "author": book.author,
                    "available": book.available
                })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    # Load Books from JSON
    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                for item in data:

                    if item["type"] == "ebook":
                        book = EBook(
                            item["title"],
                            item["author"],
                            item["file_size"],
                            item["available"]
                        )

                    else:
                        book = Book(
                            item["title"],
                            item["author"],
                            item["available"]
                        )

                    self.books.append(book)

        except FileNotFoundError:
            self.books = []

        except json.JSONDecodeError:
            print("Error reading books.json file.")
            self.books = []


# Create Library Object
library = Library()


# Main Menu
while True:

    print("\n================================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            library.search_book()

        elif choice == 4:
            library.borrow_book()

        elif choice == 5:
            library.return_book()

        elif choice == 6:
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")