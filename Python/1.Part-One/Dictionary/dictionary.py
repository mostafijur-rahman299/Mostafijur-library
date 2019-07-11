
dict={
    'brand':'squre',
    'model':34,
    'year':2017
}

x=dict.get('year')
print(x)


#change the value

dict['year']=2016
print(dict)

#add value

dict['color']='red'
print(dict)

#len
print(len(dict))

#delete the item and key
del dict['model']
print(dict)

#automatically delete the last item
dict.popitem()
print(dict)


#delete the specific key
dict.pop('year')
print(dict)


#delete the dictionary
del dict
print(dict)

#clear the dictionary
dict={
    'brand':'squre',
    'model':34,
    'year':2017
}
dict.clear()
print(dict)


thisdict =	dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)


# copy to another dictionary
dictionary={

    'dhaka':20837,
    'chitagong':342335,
    'bogra':87868,
    'naogaon':887346,
    'joypurhat':234545

}

a=dictionary.copy()
print(a)
a['thakurgaon']=3448574
print(a)


# update the dictionary
dictionary={

    'dhaka':20837,
    'chitagong':342335,
    'bogra':87868,
    'naogaon':887346,
    'joypurhat':234545

}

dictionary2={
    'rongpur':34232334,
    'dinajpur':78687,
    'rajsahi':987876
}

dictionary.update(dictionary2)
print(dictionary)
