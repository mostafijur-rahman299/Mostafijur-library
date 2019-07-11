
class Person():

    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return f'{self.__class__.__name__} class,obj name:{self.name}'

p1=Person('Sajib')
print(p1)
