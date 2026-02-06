 📅 Day 30 – map(), filter(), and reduce() in Python

Today I learned functional programming tools in Python: `map()`, `filter()`, and `reduce()`.  
These functions help write clean, concise, and readable code when working with lists and other iterables.

---

## 🔹 map()
Applies a function to each element of an iterable.

```python
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)
🔹 filter()
Filters elements based on a condition.

numbers = [10, 25, 30, 47, 50]
result = list(filter(lambda x: x > 25, numbers))
print(result)
🔹 reduce()
Reduces an iterable to a single value.

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)
🚀 Practical Example
from functools import reduce

scores = [45, 67, 89, 34, 76, 90]

updated = list(map(lambda x: x + 5, scores))
passed = list(filter(lambda x: x >= 50, updated))
total = reduce(lambda x, y: x + y, passed)

print("Updated:", updated)
print("Passed:", passed)
print("Total:", total)
