# Arberitery number of arguments
def students(*student_name):
    print(student_name,type(student_name))
    for student in student_name:
        print(student)

students('bill','steave','jonathon','milla')


#######################
def students1(captain,*student_name):
    print('Captain:',captain)
    print('General students:',student_name)

students1('mahmud','sajib','meahm','lima')


########################################

def arg_some(args,args_1,args_2,args_3):
    print(args)
    print(args_1)
    print(args_2)
    print(args_3)

args=(1,23,3,4)
arg_some(*args)

args=[1,23,3,4]
arg_some(*args)

args={1,23,3,4}
arg_some(*args)
