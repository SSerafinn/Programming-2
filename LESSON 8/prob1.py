#JEEPNEY FARE

# Given a list of jeepney fare in pesos, create a new list na mag dadagdag ng 5 pesos
# on the jeepney fare using list comprehension

fares = [13.0, 15.0, 19.0, 20.0]

#[expression for items in iterable if condition]
fare_updated = [fare + 5 for fare in fares]

print(fare_updated)