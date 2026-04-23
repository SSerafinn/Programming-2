inventory = [
    {"item": "Noodles",  "price": 8.50,  "stock": 24},
    {"item": "Sardines", "price": 15.00, "stock": 12},
    {"item": "Rice",     "price": 52.00, "stock": 5},
    {"item": "Soda",     "price": 17.00, "stock": 30},
]

#Total value = price x stock
#List Comprehension
values = [i["price"] * i["stock"] for i in inventory]
print(values)


highest_value = max(inventory, key = lambda i :i["price"] * i["stock"] )

print(highest_value)


