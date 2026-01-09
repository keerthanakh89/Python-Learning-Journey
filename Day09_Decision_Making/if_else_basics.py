# Day 9 - Decision Making (if-else)

age = int(input("Enter age: "))

# Logical operators (and, or)
if age >= 0 and age < 5:
    print("Free bus ticket")

elif age >= 60 or age == 59:
    print("Senior citizen discount")

else:
    print("Full ticket price")

    # Nested if
    if age >= 18:
        print("Adult passenger")
    else:
        print("Child passenger")
