#Problem 6 - Gym Membership

membership = input("Enter your membership status (Regular, VIP, or Premium): ")
age = int(input("Enter your age: "))

if membership == "Regular":
    if age < 18:
        price = 50.0
    elif age >= 18 and age <= 64:
        price = 100.0
    else:
        price = 75.0
elif membership == "VIP":
    if age < 18:
        price = 75.0
    elif age >= 18 and age <= 64:
        price = 150.0
    else:
        price = 112.5
elif membership == "Premium":
    if age < 18:
        price = 100.0
    elif age >= 18 and age <= 64:
        price = 200.0
    else:
        price = 150.0
else:
    print("Invalid membership status entered.")
    exit()

print(f"Price: ${price:.2f}")