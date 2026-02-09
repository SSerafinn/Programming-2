import math

num = int(input("Enter an integer: "))

square_root = int(math.sqrt(num))
is_perfect_square = square_root * square_root == num
cube = round(num ** (1/3)) 
is_perfect_cube = cube * cube * cube == num


if is_perfect_square:
    if is_perfect_cube:
        print("Perfect in every way")
    else:
        print("Nothing special")
else:
    if is_perfect_cube:
        if num % 2 == 0:
            print("Perfect in every way")
        else:
            print("Perfect in an odd way")
    else:
        print("Nothing Special")


