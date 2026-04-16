#LIST COMPREHENSION


#[expression for item in iterable if condition]
#Create a list for grades greater than 75 using comprehension

#grades = [97,67,75,89,81]
test = ["97","67"]


#scaled = [ for grade in grades]
passing = [grade for grade in grades if grade >= 75]
conv = [int(number) for number in test if number > "0"]

print(conv)

#for grade in grades:
#    scaled.append(round(grade * 1.05, 2))
     

print(passing)