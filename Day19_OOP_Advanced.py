# Day 19 - Advanced OOP Concepts in Python

# 1. Getters and Setters (Encapsulation)
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


student = Student("Chandan", 22)
print("Name:", student.get_name())
student.set_name("Darshan")
print("Updated Name:", student.get_name())
#3.method overloading
class Calculator:
    def multiply(self, a, b, c=None):
        if c is None:
            return a * b
        else:
            return a * b * c
calc = Calculator()
print(calc.multiply(2, 3))        # 6
print(calc.multiply(2, 3, 4))     # 24

# 2. Method Overriding
class Parent:
    def show(self):
        print("This is Parent class")


class Child(Parent):
    def show(self):
        print("This is Child class (Overridden method)")


obj = Child()
obj.show()


# 3. Abstract Classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick or self-start")


bike = Bike()
bike.start()

print("Day 19: Advanced OOP concepts practiced successfully")
