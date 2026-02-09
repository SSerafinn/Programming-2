x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

j = x == y and y == z and z == x

print(j)
if j:
    print("Triangle is equilateral")
else:
    print("Triangle is not equilateral")
    

#if x == y and y==z and z==x:
#    print("Triangle is equilateral")