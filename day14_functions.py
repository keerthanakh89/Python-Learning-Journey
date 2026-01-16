# Day 14 - Functions in Python (Complete Example)

# Global variable
course = "Python"

def greet():
    """Function with no parameters"""
    print("Welcome to the Python course!")

def greet_user(name="Student"):
    """Function with default parameter"""
    print(f"Hello, {name}! Welcome to the {course} course.")

def add_numbers(a, b):
    """Function with parameters and return value"""
    return a + b
def eligibility_check(age):
    """Decision making inside function"""
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

# Function calls
greet()

greet_user()
greet_user("Keerthana")

result = add_numbers(10, 20)
print("Sum:", result)

status = eligibility_check(19)
print("Eligibility Status:", status)
