def get_numbers_of_days():
    while True:
        days= int(input("Enter number of Days: "))
        if days >= 1:
            return days
        else:
            print("Invalid Input: ")
            
def get_late_minutes(day):
    while True:
        minutes = int(input(f"Enter minutes late for day {day}: "))
        if minutes >= 0:
            return minutes
        else:
            print("Invalid Input")
       
def compute_total (late_list):
    total = 0
    for minutes in late_list:
        total += minutes
    return total

def compute_total_days (late_list):
    count = 0
    for minutes in late_list:
        if minutes > 0:
            count += 1
    return count

def main():
    days = get_numbers_of_days()

    late_list = []
    
    for day in range(1, days + 1):
            late_list.append(get_late_minutes(day))
    print("")
    
    total = compute_total(late_list)
    total_days = compute_total_days(late_list)
    worst = max(late_list)

    print(f"Late minute list: {late_list}")
    print(f"Total late minute: {total}")
    print(f"Late days: {total_days}")
    print(f"Worst late minute: {worst}")
    
main()