number = input("Enter an integer: ")

sum = 0
index = 0

while index < len(number):
    sum += int(number[index])
    index += 1
    
print(sum)