def categorize_temp(temp):
    if temp <= 15:
        return "Cold"
    elif temp <= 30:
         return "Warm"
    elif temp > 30:
        return "Hot"
    else:
        return "Wrong Temp"

def display_categories(temps):
    for temp in temps:
        print(f"{temp} = {categorize_temp(temp)}")
    
def main():
    days = int(input("How many days: "))
    
    if days == 0:
        print("No temperature to display")
    else:
        temps = []
        for i in range (1, days + 1):
            temps.append(float(input(f"Temp for {i}: ")))
        display_categories(temps)
        
main()