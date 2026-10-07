# Student Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Muskan", 20, "AI")
student2 = Student("Ali", 22, "Computer Science")

student1.introduce()
print()

student2.introduce()


# Employee Class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Muskan", 50000)

print()
employee1.show_details()


# Car Class

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(self.brand, self.model, "is starting")

    def stop(self):
        print(self.brand, self.model, "is stopping")


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print()
print("Car 1:", car1.brand, car1.model, car1.year)
car1.start()

print()
print("Car 2:", car2.brand, car2.model, car2.year)
car2.start()
car2.stop()