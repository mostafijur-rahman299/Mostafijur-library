class A:
    def bhow(self):
        print('show in A')
        
class B(A):
    def show(self):
        print('show in B')
        
obj = B()

obj.show()
