class X:
    def __init__(self,name):
        self.name=name
        print(self.name, " created")

    def __del__(self):
        print(self.name, " distroyed")


objects=X('sajib')
