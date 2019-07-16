class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(self.name,self.age)

    def change_name(self,name):
        self.name=name

bill=person('sajib','34')
bill.details()
bill.name='saj'
bill.details()
bill.change_name('hey')
bill.details()
