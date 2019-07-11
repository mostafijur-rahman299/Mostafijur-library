
def class_captain_list(Captain,**captain):
    print('Principal:',Captain)
    print('Others:',captain)

class_captain_list(Captain='Mahmudsajib',first_captain='saib',
                    second_captain='mahmud',third_captain='lima')



def some_kwarg(kwargs,kwargs_1,kwargs_2):
    print(kwargs)
    print(kwargs_1)
    print(kwargs_2)

kwargs = {"kwargs":78,"kwargs_1":67,"kwargs_2":78}
some_kwarg(**kwargs)
