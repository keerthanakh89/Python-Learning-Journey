# Day 7 - Lists, Tuples, and Sets

# LIST
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print("List:", fruits)

# TUPLE
genders = ("male", "female", "others")
print("Tuple:", genders)
print("First tuple element:", genders[0])

# SET
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)  # duplicates removed

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))
