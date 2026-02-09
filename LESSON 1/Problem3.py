num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("numbers have the same sign")
else:
    print("numbers are not the same sign")