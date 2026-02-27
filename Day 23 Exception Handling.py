# Day 23 - Errors and Exception Handling in Python
# -------------------------------
# Syntax Error Example (commented)
# -------------------------------
# if True
#     print("Hello")   # Missing colon causes SyntaxError

# -------------------------------
# Runtime Error Example
# -------------------------------
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero")


# -------------------------------
# Handling ValueError
# -------------------------------
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid value conversion")


# -------------------------------
# Multiple Exception Handling
# -------------------------------
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid integer")


# -------------------------------
# Using else block
# -------------------------------
try:
    n = int(input("Enter another number: "))
    print(20 / n)
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Calculation successful")


# -------------------------------
# Using finally block
# -------------------------------
try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program End")


# -------------------------------
# Homework Example 1: Age Verifier
# -------------------------------
try:
    age = int(input("Enter your age: "))
    print("Years to reach 100:", 100 - age)
except ValueError:
    print("Invalid age entered")


# -------------------------------
# Homework Example 2: Safe Divider
# -------------------------------
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
