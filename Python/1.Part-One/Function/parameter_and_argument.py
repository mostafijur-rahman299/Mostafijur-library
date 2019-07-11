def full_name(first_name,last_name):
    return first_name+ " "+last_name

a=full_name('Sajib','Mahmud')
b=full_name('mahmud','sajib')
print(b)
print(a)

## pass argument with kwards

def full_name(first_name,last_name):
    return first_name+' '+last_name

name=full_name(first_name='sajib',last_name='mahmud')
print(name)


##################3
#positinal argument follows kwargs
def person_details(name,age,country):
    print(name,age,country,sep='|')

person_details('sajib',34,country='us')

##########################

def person_details1(name,age,country='Bangladesh'):
    print(name,age,country,sep='|')

person_details1('sajib',34)
person_details1('mahmudsajib',23,'USA')

##################3
def person_details1(name='',age,country='Bangladesh'):
    print(name,age,country,sep='|')

person_details1('sajib',34)
person_details1('mahmudsajib',23,'USA')

############################
