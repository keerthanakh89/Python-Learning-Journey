# Day 12 - Lists & Dictionaries with For Loops

numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num
print("Total:", total)

student = {"name": "Keerthana", "age": 20}
for key, value in student.items():
    print(key, value)
# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# Dictionary comprehension
square_dict = {x: x * x for x in range(1, 6)}
print(square_dict)

# List input using split
values = input("Enter numbers: ").split()
values = [int(x) for x in values]
print(values)

