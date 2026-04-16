#Long name filter

#Given a list of names, if the names has more than 6 characters store in a 
#seperate list

names = ["JP", "JD", "JC", "Thessalonica", "Vladimir", "Renz", "Agustin"]

long_names = [name for name in names if len(name) > 6]

print(long_names)