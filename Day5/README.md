Day-5: Object-Oriented Programming & Library Management System

OOP Practice

Object-Oriented Programming (OOP) is a programming approach where we organize code using classes and objects.

In this task, I practiced:

* Classes and objects
* Attributes and methods
* Constructors (`__init__`)
* `self` keyword
* Creating multiple objects

I created `Student`, `Employee`, and `Car` classes.

Inheritance

Inheritance allows a child class to use the properties and methods of a parent class.

In my Library Management System, I used inheritance between:

* `Book` → Parent class
* `EBook` → Child class

The `EBook` class inherits from the `Book` class and also overrides the `show_details()` method.

Library Management System

I created a console-based Library Management System using Python and OOP.

The system can:

* Add a new book
* View all books
* Search for a book
* Borrow a book
* Return a book
* Save book data in a JSON file
* Load book data when the program starts
* Handle invalid user input

JSON

I used `books.json` to store book records. This allows the data to remain saved even after the program is closed.

Exception Handling

I used exception handling to prevent the program from crashing when the user enters invalid input or when the JSON file has an issue.

Challenges

One challenge was handling the JSON data correctly when loading and saving books. I solved this by storing the book type and other information in the JSON file.

Another challenge was handling invalid user input. I used `try` and `except` to handle these errors.

Conclusion

This task helped me understand OOP, inheritance, JSON file handling, and exception handling. I also learned how to build a simple structured Python application.
