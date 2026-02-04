# Day 28 - Decorators (Complete Example)

# Creating a decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


# Using decorator
@my_decorator
def say_hello():
    print("Hello, welcome to Python!")


# Calling the decorated function
say_hello()


print("--------------------------------")

# Decorator with arguments
def login_required(func):
    def wrapper(user):
        if user == "admin":
            print("Access granted")
            func(user)
        else:
            print("Access denied")
    return wrapper


@login_required
def dashboard(user):
    print("Welcome to dashboard,", user)


# Calling function with different users
dashboard("admin")
dashboard("guest")


print("--------------------------------")

# Decorator for logging
def log_function(func):
    def wrapper():
        print("Function name:", func.__name__)
        func()
    return wrapper


@log_function
def sample_task():
    print("Task is running")


sample_task()
