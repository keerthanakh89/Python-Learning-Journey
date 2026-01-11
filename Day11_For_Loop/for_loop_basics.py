# Day 11 - For Loop Basics

cities = ["Bengaluru", "Mysuru", "Hubballi"]

for city in cities:
    print(city)
# range() function
for i in range(1, 6):
    print(i)

# enumerate()
for index, city in enumerate(cities):
    print(index, city)

# break and continue
for num in range(1, 6):
    if num == 3:
        continue
    if num == 5:
        break
    print(num)

# for-else
for i in range(3):
    print(i)
else:
    print("Loop completed")

# dictionary iteration
student = {"name": "Keerthana", "age": 20}
for key, value in student.items():
    print(key, value)

# nested for loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

