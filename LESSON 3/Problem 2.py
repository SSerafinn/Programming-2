#Problem 2 - Counting Uppercase Letters

sentence = input("Enter a sentence: ")

uppercaseCount = 0

for i in range(len(sentence)):
    c = sentence[i]
    if c.isupper():
        uppercaseCount += 1

print(f"Number of uppercase letters:{uppercaseCount}")


#Alternative Solution

sentence = input("Enter a sentence: ")

uppercaseCount = 0

for c in sentence:
    if c.isupper():
        uppercaseCount += 1

print(f"Number of uppercase letters: {uppercaseCount}")
