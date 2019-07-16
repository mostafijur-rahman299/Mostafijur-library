

class Alien:
    legs=6
    def __init__(self,name):
        self.name=name

alien=Alien('Maven')
alien2=Alien('Oven')
alien.name='sajib'
print(alien.name,alien2.name)
alien.legs=78
print(alien.legs,alien2.legs)
Alien.legs=100
print(alien.legs,alien2.legs)
alien.__class__.legs=200
print(alien.legs,alien2.legs)
