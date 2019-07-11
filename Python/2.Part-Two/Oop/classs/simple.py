class Resturant():
    name=''
    owner=''

    def details(self):
        print(self.name,self.owner)

    def details_with_address(self,address,nme):
        print(self.name,self.owner)
        print(address)
        print(nme)

resturant1=Resturant()
resturant1.name='Himalay restora'
resturant1.owner='sajib'
resturant1.details_with_address('bogra','jis')
