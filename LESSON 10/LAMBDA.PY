#lambda function - is a small, anon function defined in a single expression


def square(n):
    return n**2

s_n = lambda n: n**2


def add_ten (n):
    return n + 10

add_ten = lambda n: n+10


#print(s_n(5))

#lambda parameters : expression


def add_two_numbers (x,y):
    return x+y

add_two_numbers = lambda x, y : x + y
print(add_two_numbers(6,7))

