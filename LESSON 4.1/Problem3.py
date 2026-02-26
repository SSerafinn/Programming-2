def num_days():
    while True:
        try:
            number_of_days = int(input("Enter number of days: "))
            if number_of_days >= 0:
                return number_of_days
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")
            
def num_cal(index):
    while True:
        try:
            number_of_calories = int(input("Enter number of day calories: "))
            if number_of_calories >= 0:
                return number_of_calories
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")
            
def main():
    number_of_days = num_days()
    
    cal_list = []
    tot_cal = 0
    avg_cal = 0
    day_over = 0
    
    for i in range (1, number_of_days + 1):
        number_of_calories = num_cal(i)
        cal_list.append(number_of_calories)
        
        tot_cal += number_of_calories
        
        if number_of_calories >= 500:
            day_over += 1
         
    avg_cal = tot_cal / num_days
    
    print("")
    print(f"Calorie List: {cal_list}")
    print(f"Total Calories: {tot_cal}")
    print(f"Average Calories: {avg_cal}")
    print(f"Days burned >= 500 calories: {day_over}")
        