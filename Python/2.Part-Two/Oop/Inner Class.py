class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        # create object inside class
        self.lap = self.Laptop()
        
    def show(self):
        self.lap.show()
        print(self.name, self.age )
        
    class Laptop:
        def __init__(self):
            self.brand = 'Apple'
            self.cpu = 'i5'
            self.ram = 16
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
            
# create object outside class
lap1 = Student.Laptop()

s1 = Student('mahmud', 21)
s1.show()
