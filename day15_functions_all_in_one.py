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
