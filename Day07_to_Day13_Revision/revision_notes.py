# Revision: Day 7 to Day 13 (All Concepts in One File)
# Covers: Tuples, Sets, Decision Making, Loops, Comprehensions, Debugging

print("---- Day 7: Tuples and Sets ----")

# Tuple
fruits = ("apple", "banana", "cherry")
print("Tuple:", fruits)
print("First fruit:", fruits[0])

# Set
numbers = {1, 2, 2, 3, 4}
print("Set (duplicates removed):", numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))


print("\n---- Day 9: Decision Making ----")

age = 25

if age < 5:
    print("Free ticket")
elif age >= 60:
    print("Senior citizen discount")
else:
    print("Normal ticket")

# Logical operators
if age >= 18 and age < 60:
    print("Adult passenger")

# Nested if
if age >= 18:
    if age >= 21:
        print("Eligible for adult services")
    else:
        print("Not eligible")


print("\n---- Day 10: While Loop ----")

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    if i == 5:
        break
    print("While loop value:", i)
    i += 1


print("\n---- Day 11: For Loop ----")

# range()
for i in range(1, 4):
    print("Range value:", i)

# enumerate()
cities = ["Bengaluru", "Mysuru", "Hubballi"]
for index, city in enumerate(cities):
    print(index, city)

# for-else
for i in range(3):
    print("Loop i:", i)
else:
    print("For loop completed")

# Dictionary iteration
student = {"name": "Keerthana", "age": 20}
for key, value in student.items():
    print(key, ":", value)


print("\n---- Day 12: Comprehensions ----")

# List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# Dictionary comprehension
square_dict = {x: x * x for x in range(1, 6)}
print("Square dictionary:", square_dict)

# List input using split
input_values = "1 2 3 4 5".split()
num_list = [int(x) for x in input_values]
print("Input list:", num_list)


print("\n---- Day 13: Debugging & Execution Flow ----")

count = 0
while count < 3:
    print("Count:", count)
    count += 1

print("Loop finished correctly")

# Tracing logic
x = -5
if x > 0:
    print("Positive number")
else:
    print("Negative number")

