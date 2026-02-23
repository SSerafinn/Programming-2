while True:
    try:
        n = int(input("Enter number of days recorded: "))
        if n >= 1:
            break
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")

late_list = []

for day in range(1, n + 1):
    while True:
        try:
            minutes = int(input(f"Enter minutes late for day {day}: "))
            if minutes >= 0:
                late_list.append(minutes)
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

total = 0
for minutes in late_list:
    total += minutes

late_days = 0
for minutes in late_list:
    if minutes > 0:
        late_days += 1


worst = max(late_list)

print("\nLate minutes list:", late_list)
print("Total late minutes:", total)
print("Late days:", late_days)
print("Worst lateness:", worst)