word = input("Enter a string: ").lower()

a_counter = 0
b_counter = 0

for i in range(len(word)):
    if word[i] == "a":
        a_counter +=1
    elif word[i] == "b":
        b_counter +=1
        
print(f"Number of 'a' occurences: {a_counter}")
print(f"Number of 'b' occurences: {b_counter}")