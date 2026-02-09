try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    
    if x == y:
        print("Numbers are equal.")
    else:
        print("Numbers are not equal.")
except ValueError:
    print("Invalid Charater, Enter an integer.")
except:
    print("Error")

