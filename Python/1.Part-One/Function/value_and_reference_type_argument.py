#value type

num=100
def change_num(num):
    num=num+200
    print(num)

change_num(num)
print(num)



##################################
#Reference type argument

num_list=[1,2,3,4,5]
num_dict={'one':1,'two':2,'three':3}
def change_num(list,dict):
    del list[0]
    list[-1]=50

    del dict['one']
    dict['three']=33
    print('Inner list:',list)
    print('Inner dict:',dict)

print("Before coll function")
print('Outer list:',num_list)
print('Outer dict:',num_dict)

change_num(list=num_list,dict=num_dict)

print("After coll function")
print('Outer list:',num_list)
print('Outer dict:',num_dict)
