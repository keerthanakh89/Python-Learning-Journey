# Dictionary - Complete Example

# Creating a dictionary
student = {
    "name": "Keerthana",
    "age": 20,
    "branch": "CSE"
}

print("Original dictionary:", student)

# Accessing elements
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding new element
student["college"] = "VTU"
print("After adding college:", student)

# Updating value
student["age"] = 21
print("After updating age:", student)

# Removing elements
student.pop("branch")
print("After removing branch:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Checking key existence
if "name" in student:
    print("Name key exists")

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Clearing dictionary
student.clear()
print("After clear():", student)
