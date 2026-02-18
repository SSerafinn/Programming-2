#Problem 1 - Product of numbers

number = int(input("Enter a number: "))

product = 1

for i in range(1, number + 1):
    product *= i

print(f"Product:{product}")