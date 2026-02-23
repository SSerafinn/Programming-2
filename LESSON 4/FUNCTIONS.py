#Example 1

#def add(num1, num2, num3):
#    return num1 + num2
#
#results = add(5, 9)
#print(results)

#Example 2

#def add(num1, num2):
#    print(num1 + num2)
#
#add(3,6)

def add(num1, num2, num3=0):
    return num1 + num2 + num3
    
def subract(num1, num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    return num1 / num2

def main():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input("Enter Operator (+,-,/,*): ")
    
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subract(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    else:
        print("Wrong Operator")
        
    print(result)
    
main()