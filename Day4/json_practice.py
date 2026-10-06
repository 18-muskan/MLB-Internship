# JSON Practice

import json


# Step 1: Store student information in a JSON file

students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 20,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 21,
        "course": "Machine Learning"
    }
]

file = open("students.json", "w")

json.dump(students, file, indent=4)

file.close()

print("Student information has been saved.")


# Step 2: Read data from the JSON file

file = open("students.json", "r")

students = json.load(file)

file.close()

print("\nStudent information:")

for student in students:
    print(student)


# Step 3: Update an existing student's information

for student in students:
    if student["id"] == 2:
        student["age"] = 22

print("\nSara's age has been updated.")


# Save the updated information

file = open("students.json", "w")

json.dump(students, file, indent=4)

file.close()


# Step 4: Add a new student

new_student = {
    "id": 3,
    "name": "Ahmed",
    "age": 23,
    "course": "Data Science"
}

students.append(new_student)

print("New student has been added.")


# Save the new student in the JSON file

file = open("students.json", "w")

json.dump(students, file, indent=4)

file.close()


# Display final data

print("\nFinal student information:")

for student in students:
    print(student)
