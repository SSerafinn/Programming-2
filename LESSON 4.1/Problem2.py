def num_orders():
    while True:
        try:
            number_of_orders = int(input("Enter number of orders: "))
            if number_of_orders >= 1:
                return number_of_orders
            else:
                print("Ïnvalid Input")
        except:
            print("Invalid Input")
            
def amount_orders(index):
    while True:
        try:
            amount_of_orders = int(input(f"Enter amount of order {index}: "))
            if amount_of_orders >= 1:
                return amount_of_orders
            else:
                print("Ïnvalid Input")
        except:
            print("Invalid Input")

def main():  
    number_of_orders = num_orders()
    
    total = 0
    average = 0
    big_orders = 0
    
    for i in range (1, number_of_orders +1):
        amount_of_orders = amount_orders(i)
        
        total += amount_of_orders
        
        if amount_of_orders >= 100:
            big_orders += 1
    
    average = total / number_of_orders
    
    print("")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Big Orders: {big_orders}")
    
        
main()