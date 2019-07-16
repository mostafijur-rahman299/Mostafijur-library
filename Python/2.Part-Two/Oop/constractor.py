
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def details(self):
        print(self.name,self.age)



bill=person('sajib',33)
bill.details()
