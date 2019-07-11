list_of_car=['car','toyota','bmw','mesetice']

# append item
list_of_car.append('pajero')
print(list_of_car)

#item insert with location
list_of_car.insert(2,'sajib')
print(list_of_car)


list_of_car+=['pajero']

#delte a number
list_of_car.pop()
print(list_of_car)

list_of_car.remove('bmw')
print(list_of_car)

del list_of_car[1:4]
print(list_of_car)

# delete a item with location
del list_of_car[3]
print(list_of_car)

# remove a list with give list item
list_of_car.remove('car')
print(list_of_car)

# reverse a list item
sorted=sorted(list_of_car,reverse=True)
print(sorted)

list_of_car.sort()
print(list_of_car)

# extend about list
a=[3,4,5,4]
b=[6,5,4,4]

a.extend(b)
print(a)
