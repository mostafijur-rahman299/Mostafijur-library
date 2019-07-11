person="Mr.x's age is 66"
print(person)
#interpolation modern way
person="{name},s age in {age}"
print(person.format(name='Mr.x',age=66))

#interpolation old way
person="%s\'s age is %d"
print(person %('Mr.x',55))
