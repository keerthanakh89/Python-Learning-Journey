# Day 15 - Python Functions (All Concepts in One Example)

# Global variable
course = "Python"

def student_details(name, age=18, *skills, **extra_info):
    """
    Demonstrates:
    - default parameter (age)
    - *args (skills)
    - **kwargs (extra_info)
    - local vs global variable
    """

    # Local variable
    status = "Active"

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")  # using global variable
    print(f"Status: {status}")

    print("Skills:")
    for skill in skills:
        print("-", skill)

    print("Extra Info:")
    for key, value in extra_info.items():
        print(f"{key}: {value}")
# Lambda function
square = lambda x: x * x

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Nested function
def result_analysis(marks):
    def grade():
        if marks >= 75:
            return "Distinction"
        elif marks >= 50:
            return "Pass"
        else:
            return "Fail"
    return grade()
