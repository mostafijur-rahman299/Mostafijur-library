
#Objects comparision........ "==" vs "is" operator

x=[1,2,3]
xx=x
print(x == xx)
print(x is xx)

"""
"==" is check the content of object and "is" is check the identity or memory address

"""
x=[1,2,3]
y=list(x)

print(y == x)
print(y is x)

print(id(x))
print(id(y))
