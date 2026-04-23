#          0  1  2  3  4
#         -5 -4 -3 -2 -1

# range + 1 lagi kapag gagamit ng range
#print(grades[1:4])
#
#print(grades[::])

# [81, 92, 88] -> try to print this one




#list methods

#append method 
#list.append(x) x=item to add to our list


#insert
#list.insert(i, x) i=index of the list x=item in the list
#it inserts item before the index


#list.remove(x) x = first instance of the item
#list.reverse()
#list.count(x) x=how many times this value exist


# List iteration

# for value in list:
#    print value


grades = [88,74,92,60,92,81,56]

#LIST COMPREHENSION - BUILDING A NEW LIST FROM A LOOP
passed = [value for value in grades if value >= 75]

print(passed)




    
