## Day 27 – Python match-case Statement

### What I Learned:
- Introduction to Python `match-case` (Python 3.10+)
- Used as an alternative to multiple if-elif-else conditions
- Makes conditional logic cleaner and more readable
- Useful for handling multiple fixed values

### Example:
num = int(input("Enter a number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Some other number")
