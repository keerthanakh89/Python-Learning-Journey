# Day 17 - Object Oriented Programming (OOP)
# Topic: Class, Object, __init__ constructor, self keyword

# Example 1: Simple class with constructor
class Human:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def walk(self):
        print(self.name, "is walking")

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
person1 = Human("Chandan", 22)
person2 = Human("Darshan", 20)

person1.walk()
person1.details()

print("---------------")

person2.walk()
person2.details()


# Example 2: Constructor with default value
class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
        print()


# Creating employee objects
emp1 = Employee("Keerthana", "Developer")
emp2 = Employee("Asha", "Tester", 25000)

emp1.display_details()
emp2.display_details()


print("Day 17 OOP practice completed")
