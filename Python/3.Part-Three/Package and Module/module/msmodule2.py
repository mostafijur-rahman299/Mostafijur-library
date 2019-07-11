import msmodule
print(msmodule.sum(2,3))


from msmodule import sub
print(sub(4,7))


from msmodule import *
print(sum(5,4))

from msmodule import MathClass
object=MathClass(3,4)
print(object.mul())

from msmodule import MathClass as math
obj=math(4,3)
print(obj.div())
