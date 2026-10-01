# Python Fundamentals - Day 1

# Variables and Data Types
name = "Muskan"
age = 21
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)


# List
skills = ["Python", "Machine Learning", "AI"]
print("Skills:", skills)


# Tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)


# Set
languages = {"Python", "Python", "SQL"}
print("Languages:", languages)


# Dictionary
student = {
    "name": "Muskan",
    "semester": 6,
    "field": "AI/ML"
}

print("Student:", student)


# Function
def greet(name):
    return "Hello, " + name


print(greet("Muskan"))


# Conditional Statement
if age >= 18:
    print("Adult")
else:
    print("Minor")