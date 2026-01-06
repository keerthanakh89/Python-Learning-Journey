# Day 6 - Python Lists
# Creating a list
l = [10, 20, 30, 40, 50]
print("Original list:", l)

# Accessing list elements
print("First element:", l[0])
print("Last element:", l[-1])

# Modifying list (changing specific element)
l[1] = 25
print("After changing second element:", l)

# Adding elements
l.append(60)        # add at end
l.insert(2, 15)     # add at specific position
print("After append and insert:", l)

# Removing elements
l.remove(40)        # remove specific value
l.pop()             # remove last element
print("After remove and pop:", numbers)

# Slicing
print("Sliced list (index 1 to 3):", l[1:4])

# List functions
print("Length of list:", len(l))
print("Sorted list:", sorted(l))
print("Sum of elements:", sum(l))

# List methods
print("Index of 30:", l.index(30))
print("Count of 25:",l.count(25))

l.reverse()
print("Reversed list:",l)

l.sort()
print("Sorted list using sort():",l)

# Nested list (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix:", matrix)
print("Element at row 2, column 1:", matrix[1][0])

# Clear list
l.clear()
print("List after clear():",l)
