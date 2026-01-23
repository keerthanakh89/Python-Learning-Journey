# Day 16 – Object Oriented Programming (OOP) in Python

# -------------------------------
# Procedural Programming Example
# -------------------------------
def display_student(name, marks):
    print("Name:", name)
    print("Marks:", marks)

display_student("Keerthana", 85)

print("-" * 30)

# -------------------------------
# OOP: Class and Object
# -------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name        # Attribute
        self.marks = marks      # Attribute

    def display_details(self):  # Method
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Keerthana", 85)
student1.display_details()

print("-" * 30)

# -------------------------------
# Multiple Objects
# -------------------------------
student2 = Student("Anita", 90)
student3 = Student("Rahul", 78)

student2.display_details()
student3.display_details()

print("-" * 30)

# -------------------------------
# Real-World Example (E-Commerce)
# -------------------------------
class DisplayModule:
    def show_products(self):
        print("Displaying products")

class OrderManagement:
    def place_order(self):
        print("Order placed successfully")

class Payment:
    def make_payment(self):
        print("Payment completed")

display = DisplayModule()
order = OrderManagement()
payment = Payment()

display.show_products()
order.place_order()
payment.make_payment()

print("-" * 30)

# -------------------------------
# Why OOP?
# -------------------------------
print("OOP helps in:")
print("- Code reusability")
print("- Better structure")
print("- Real-world modeling")
print("- Easy maintenance")
