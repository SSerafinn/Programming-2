#Product Inventory

#List all of the name of the products or items in the given dictionary in a seperate
#list


inventories = [
    {"items": "Sardinas", "price": 16, "stock": 20},
    {"items": "Brown Sugar", "price": 22, "stock": 78},
    {"items": "Ipad", "price": 18999, "stock": 5},
    {"items": "Argentina Cornbeef", "price": 56, "stock": 43},
    {"items": "Whiskey", "price": 799, "stock": 54},
]


items_names = [inventory["items"] for inventory in inventories]

#if items has a stock that is less than 20
low_stock = [inventory["items"] for inventory in inventories if inventory["stock"] < 20]

print(items_names)
print(low_stock)