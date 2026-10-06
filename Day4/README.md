Day 4 - File Handling and JSON

What I Learned

In Day 4, I learned about file handling and JSON in Python.

I learned how to:

* Create and write data into a file
* Read data from a file
* Append new data
* Count lines in a file
* Create JSON data
* Read JSON data
* Update JSON data
* Add new data to JSON
* Save and load student records

File Handling

I practiced the following file modes:

* `w` - Write data into a file
* `r` - Read data from a file
* `a` - Add new data to an existing file

I also learned how to use `readlines()` to count the number of lines in a file.

JSON

JSON is useful for storing data in a structured format.

I used Python's `json` module and learned:

* `json.dump()` to save data into a JSON file
* `json.load()` to read data from a JSON file

Student Record Management System

I updated my previous Student Record Management System to save student records permanently.

The system can:

1. Add a student
2. View all students
3. Search for a student
4. Update a student
5. Delete a student
6. Show total students
7. Save records in a JSON file

The program automatically loads existing student records when it starts.

Exception Handling

I also used exception handling to handle invalid inputs.

For example, if the user enters text instead of a number for age or marks, the program shows an error message instead of crashing.

Challenges

One challenge was connecting the student management system with JSON file storage.

I also had to handle invalid input and make sure that student records were saved after adding, updating, or deleting a student.

Files

* `file_handling.py` - File handling practice
* `json_practice.py` - JSON practice
* `student_record_system.py` - Persistent Student Record Management System
* `students.txt` - Sample text file
* `student_records.json` - Student records storage
* `README.md` - Day 4 documentation
