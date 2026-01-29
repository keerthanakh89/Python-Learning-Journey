# Day 22 - SOLID Principles in Python
# Learning clean, maintainable, and scalable OOP design

# ===============================
# S - Single Responsibility Principle (SRP)
# ===============================

class Student:
    def __init__(self, name):
        self.name = name

class StudentPrinter:
    def print_details(self, student):
        print(f"Student Name: {student.name}")


# ===============================
# O - Open/Closed Principle (OCP)
# ===============================

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# ===============================
# L - Liskov Substitution Principle (LSP)
# ===============================

class Bird:
    def move(self):
        print("Bird is moving")

class Sparrow(Bird):
    def move(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def move(self):
        print("Ostrich is running")


# ===============================
# I - Interface Segregation Principle (ISP)
# ===============================

class Printer:
    def print_doc(self):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_doc(self):
        print("Printing document")

    def scan(self):
        print("Scanning document")


# ===============================
# D - Dependency Inversion Principle (DIP)
# ===============================

class Keyboard:
    def type(self):
        print("Typing using keyboard")

class Computer:
    def __init__(self, input_device):
        self.input_device = input_device

    def input(self):
        self.input_device.type()


# ===============================
# Testing the Concepts
# ===============================

student = Student("Keerthana")
printer = StudentPrinter()
printer.print_details(student)

rect = Rectangle(10, 5)
circle = Circle(7)
print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())

bird1 = Sparrow()
bird2 = Ostrich()
bird1.move()
bird2.move()

mfp = MultiFunctionPrinter()
mfp.print_doc()
mfp.scan()

keyboard = Keyboard()
computer = Computer(keyboard)
computer.input()
