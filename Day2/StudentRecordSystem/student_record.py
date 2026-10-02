# Student Record Management System

students = []


# Add Student
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    subjects = {}
    
    number_of_subjects = int(input("How many subjects? "))

    for i in range(number_of_subjects):
        subject = input("Enter subject name: ")
        marks = float(input("Enter marks: "))
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

    print("\nStudent added successfully!")
    print("Average:", average)
    print("Grade:", grade)


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
        if student["roll_number"] == roll_number:
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
        if student["roll_number"] == roll_number:

            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")


# Delete Student
def delete_student():
    roll_number = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


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