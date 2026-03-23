grades = [78, 92, 85, 89, 74, 90, 75, 85, 74, 65, 32, 41, 96]

def total(list):
    total_grade = 0
    for grade in list:
        total_grade += grade
    return total_grade

def average(total, len_of_list):
    average = total/len_of_list
    return average

def highest(list):
    highest = max(list)  

def lowest(list):
    lowest = min(list)

total = total(grades)
list_len = len(grades)
average = average(total, list_len)

print(total)
print(average)

