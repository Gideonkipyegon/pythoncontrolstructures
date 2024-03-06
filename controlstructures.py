# if-else statement: Checking if a number is positive, negative, or zero
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# for loop: Printing squares of numbers in a given range
for i in range(5):
    print("Square of", i, "is", i*i)

# while loop: Finding factorial of a number
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)

# break statement: Finding the first occurrence of a target value in a list
numbers = [1, 3, 5, 7, 9, 5, 2, 4]
target = 5
for num in numbers:
    if num == target:
        print("Target found")
        break
else:
    print("Target not found")

# continue statement: Skipping even numbers in a loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass statement: Placeholder for future code implementation
for i in range(3):
    pass  # Placeholder for future code implementation

# Nested control statements: Printing a pattern using nested loops
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
