#Problem 8 - Inverted Triangle

size = int(input("Enter the size: "))

for i in range(1, size + 1):
    for j in range(size, i - 1, -1):
        print("*", end="")
    print()