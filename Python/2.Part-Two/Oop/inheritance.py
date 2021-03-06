
class Math:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self):
        return self.x+self.y
    
    
# single inheritance
class Math2(Math):
    def __init__(self,xx,yy):
        self.xx=xx
        self.yy=yy
        super().__init__(xx,yy)

    def sub(self):
        return self.xx-self.yy
    
    
 # multi level inheritance
class MathExtends(Math2):
    pass

class Math3:
    def div(self,x,y):
        return x/y
    
# mutiple inheritance
class Math4(Math2,Math3):
    def __init__(self,xxx,yyy):
        self.x=xxx
        self.y=yyy
        super().__init__(xxx,yyy)

    def mul(self):
        return self.xxx*self.yyy

    def sum(self):
        return self.x+self.y

    def show_all(self):
        print(super().sum())
        print(self.sub())
        print(self.mul())
        print(self.div(self.xxx,self.yyy))

object=Math4(3,4)
object.show_all()
