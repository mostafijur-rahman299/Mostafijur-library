class Math:
    # this is method overloading but don't suppor python
    def sum(self, a, b):
        s = a + b
        return s
    
    def sum(self, a, b, c):
        s = a + b
        return s
    
    #############################
    
    # instead of 
    def sum2(self,a=None,b=None,c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
    
obj1 = Math()

obj1.sum2(2)
