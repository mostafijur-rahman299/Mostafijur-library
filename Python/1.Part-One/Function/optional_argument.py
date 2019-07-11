#optional argument

def get_name(first_name,last_name,middle_name=''):
    complete_name=first_name
    if middle_name:
        complete_name+=' '+middle_name
    complete_name+=' '+last_name
    return complete_name

print(get_name('sajib','mahmud'))
print(get_name('sajib','mahmud','s'))
