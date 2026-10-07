# Parent Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class - Student

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Child Class - Teacher

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print("Teacher Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


# Creating objects

student1 = Student("Muskan", 20, "AI")
teacher1 = Teacher("Ahmed", 35, "Python")


# Calling methods

student1.introduce()

print()

teacher1.introduce()