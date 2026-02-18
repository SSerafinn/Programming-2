#Problem 7 - Direction Finder

direction = input("Enter a direction (N, S, E, W): ").upper()

opposite_direction = ""

if direction == "N":
    opposite_direction = "S"
elif direction == "S":
    opposite_direction = "N"
elif direction == "E":
    opposite_direction = "W"
elif direction == "W":
    opposite_direction = "E"
else:
    print("Invalid direction")
    exit(0)

print(f"Opposite direction: {opposite_direction}")