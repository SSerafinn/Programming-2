word = input("enter a word")

a_counter = 0
b_counter = 0 

for i in word:
    if i == "a":
        a_counter+=1
    elif i == "b":
        b_counter+=1
        
print(f"Number of 'a' occurences: {a_counter}")
print(f"Number of 'b' occurences: {b_counter}")