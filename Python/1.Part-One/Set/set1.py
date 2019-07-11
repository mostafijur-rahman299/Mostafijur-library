

set={3,45,6,4,3,2,6}

set.add('sajib')
print(set)

set={3,45,6,4,3,2,6}
set.clear()
print(set)

set={3,45,6,4,3,2,6}
a=set.copy()
print(a)

set.remove(10)
print(set)

"""excluded set1 to set2..set2 have any similar
 item of the set1 that is excluded..
and accecpted the unsimiler item of set1 not set2"""

set1={1,2,3,4,5,6,7}
set2={3,4,5,6,7,8,9}
result=set1.difference(set2)
print(result)

set1={1,2,3,4,5,6,7}
set2={3,4,5,6,7,8,9}
set3={8,9,3,4,5,6}
result=set1.difference(set2).difference(set3)
print(result)
print(set1)


set1={1,2,3,4,5,6,7}
set2={3,4,5,6,7,8,9}
result=set1.difference_update(set2)
print(result)
print(set1)

#discard remove the indecate item if item is not here don't give raise
set1={'a','b','j','s','i'}
set1.discard('a')
print(set1)


#remove is like to discard but it give error when the item is not didn't here
set1={'a','b','j','s','i'}
set1.remove('a')
print(set1)

#take the each item only one time
set1={1,3,4,5,6,7,8}
set2={3,4,5,6,7,1,2}
result=set1.union(set2)
print(result)

#take the common item
set1={1,3,4,5,6,7,8}
set2={3,4,5,6,7,1,2}
result=set1.intersection(set2)
print(result)

x = {"a","b","c"}
y = {"r","a","f"}
result=x.isdisjoint(y)
print(result)


x = {"a","b","c","d","e"}
y = {"c","d"}
result=y.issubset(x)
print(result)


x = {"a","b","c","d","e"}
y = {"c","d"}
result=x.issubset(y)
print(result)


x = {"a","b","c","d","e"}
y = {"c","d"}
result=x.issuperset(y)
print(result)

x = {"a","b","c","d","e"}
print(x.pop())
