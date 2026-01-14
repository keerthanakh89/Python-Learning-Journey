
# Homework Solutions - Lessons 1 to 6
# Based on mentor explained solutions
# Covers Python fundamentals clearly

# -------------------------
# Lesson 1: Basics & Print
# -------------------------
print("Hello, Python!")
print("Learning Python step by step")

# -------------------------
# Lesson 2: Variables & Data Types
# -------------------------
name = "Keerthana"
age = 20
marks = 85.5
is_student = True

print(name, age, marks, is_student)

# -------------------------
# Lesson 3: Input & Output
# -------------------------
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"My name is {user_name} and I am {user_age} years old")

# -------------------------
# Lesson 4: Strings
# -------------------------
text = "Python Programming"

print(text.upper())
print(text.lower())
print(text[0:6])          # slicing
print(len(text))          # length
print(text.replace("Python", "Java"))
# -------------------------
# Lesson 5: Operators
# -------------------------
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a > b and b < 5)
print(a == 10 or b == 5)
# -------------------------
# Lesson 6: Lists
# -------------------------
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.pop()

print(numbers)
print(numbers[1:4])
print(len(numbers))
print(sorted(numbers))
