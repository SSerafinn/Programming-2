#Problem 4 - Password Strength Checker

while True:
    password = input("Please enter a password: ")
    length = len(password)
    has_uppercase = has_lowercase = has_digit = False

    for i in range(length):
        if password[i].isupper():
            has_uppercase = True
        elif password[i].islower():
            has_lowercase = True
        elif password[i].isdigit():
            has_digit = True

    if length >= 8 and has_uppercase and has_lowercase and has_digit:
        print("Valid password")
        break
    else:
        print("Invalid password. Password should be at least 8 characters long, "
              + "and contain at least one uppercase letter, one lowercase letter, and one number.")

#Alternative Solution

while True:
    password = input("Please enter a password: ")

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if len(password) >= 8 and has_uppercase and has_lowercase and has_digit:
        print(f"Valid password")
        break
    else:
        print(f"Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.")


#More professional and advenced solution

while True:
    password = input("Please enter a password: ")

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if len(password) >= 8 and has_uppercase and has_lowercase and has_digit:
        print(f"Valid password")
        break
    else:
        print(f"Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.")
