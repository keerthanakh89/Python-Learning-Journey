# Day 18 - Four Pillars of Object Oriented Programming (OOP)

# 1. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
print("Balance:", account.get_balance())


# 2. Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()


# 3. Polymorphism
class Bird:
    def fly(self):
        print("Bird flies")


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


birds = [Bird(), Penguin()]
for b in birds:
    b.fly()


# 4. Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Car moves on road")


car = Car()
car.move()

print("Day 18: Four pillars of OOP practiced successfully")
