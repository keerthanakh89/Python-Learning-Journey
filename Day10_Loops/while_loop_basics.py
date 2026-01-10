# Day 10 - While Loop
count = 1

while count <= 5:                      # while loop
    print("Count:", count)

    # continue example
    if count == 2:
        count += 1
        continue

    # nested while loop
    inner = 1
    while inner <= 2:
        print("  Inner loop:", inner)
        inner += 1

    # break example
    if count == 4:
        print("Breaking the loop")
        break

    count += 1


# Taking user input using while loop
num = int(input("Enter a number greater than 0: "))

while num <= 0:
    print("Invalid input, try again")
    num = int(input("Enter a number greater than 0: "))

print("Valid number entered:", num)

