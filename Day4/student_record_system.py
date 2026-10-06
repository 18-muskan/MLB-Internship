# Student Record Management System

import json
import os


# This is the file where student records will be saved
FILE_NAME = "student_records.json"

students = []


# Save students to JSON file
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Load students from JSON file
def load_students():
    global students

    try:

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r") as file:
                students = json.load(file)

        else:
            students = []
            save_students()

    except json.JSONDecodeError:

        print("\nJSON file is empty or damaged.")
        students = []
        save_students()


# Add Student
def add_student():

    try:

        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")

        # Check if this roll number already exists
        for student in students:

            if student.get("roll_number") == roll_number:
                print("\nThis roll number already exists.")
                return

        age = int(input("Enter age: "))
        course = input("Enter course: ")

        subjects = {}

        number_of_subjects = int(input("How many subjects? "))

        if number_of_subjects <= 0:
            print("\nNumber of subjects must be greater than 0.")
            return

        for i in range(number_of_subjects):

            subject = input("Enter subject name: ")
            marks = float(input("Enter marks: "))

            if marks < 0 or marks > 100:
                print("\nMarks must be between 0 and 100.")
                return

            subjects[subject] = marks

        average = sum(subjects.values()) / len(subjects)

        if average >= 80:
            grade = "A"

        elif average >= 70:
            grade = "B"

        elif average >= 60:
            grade = "C"

        else:
            grade = "F"

        student = {
            "name": name,
            "roll_number": roll_number,
            "age": age,
            "course": course,
            "subjects": subjects,
            "average": average,
            "grade": grade
        }

        students.append(student)

        save_students()

        print("\nStudent added successfully!")
        print("Average:", average)
        print("Grade:", grade)

    except ValueError:

        print("\nPlease enter a valid number.")


# View All Students
def view_students():

    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n===== All Students =====")

    for student in students:

        print("\nName:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Subjects:", student["subjects"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])


# Search Student
def search_student():

    roll_number = input("Enter roll number to search: ")

    for student in students:

        if student.get("roll_number") == roll_number:

            print("\nStudent Found!")

            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Subjects:", student["subjects"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])

            return

    print("\nStudent not found.")


# Update Student
def update_student():

    roll_number = input("Enter roll number to update: ")

    for student in students:

        if student.get("roll_number") == roll_number:

            try:

                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["course"] = input("Enter new course: ")

                save_students()

                print("\nStudent updated successfully!")

                return

            except ValueError:

                print("\nPlease enter a valid age.")

                return

    print("\nStudent not found.")


# Delete Student
def delete_student():

    roll_number = input("Enter roll number to delete: ")

    for student in students:

        if student.get("roll_number") == roll_number:

            students.remove(student)

            save_students()

            print("\nStudent deleted successfully!")

            return

    print("\nStudent not found.")


# Load existing students when program starts
load_students()


# Main Menu
while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            print("\nTotal Students:", len(students))

        elif choice == "7":

            print("\nThank you for using Student Record Management System!")

            break

        else:

            print("\nInvalid choice. Please try again.")

    except Exception as e:

        print("\nSomething went wrong:", e)
