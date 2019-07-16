
#Delete the age property from the p1 object:

class Hotel():
    name=''
    owner_name=''

    def details(self):
        name=self.name
        owner=self.owner_name
        print(name,owner)

object=Hotel()
object.name='sajib'
object.owner_name='Mhmaud'
object.details()
del object.name
object.details()
object.name='sajib'
object.details()



#You can delete objects by using the del keyword:

class Hotel():
    name=''
    owner_name=''

    def details(self):
        name=self.name
        owner=self.owner_name
        print(name,owner)

object=Hotel()
object.name='Rose Hotel'
object.owner_name='Mahmudsajib'
object.details()
print("Befor Delete: ",object)
del object
print("After Delete: ",object)
