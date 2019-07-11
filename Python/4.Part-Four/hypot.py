# @Date:   2018-11-03T17:03:06+06:00
# @Last modified time: 2018-11-03T18:53:07+06:00

#Returns the length of a hypotenuse that extends from (0, 0) to (x, y). 
import math

def main():
    a = int(input())
    b = int(input())
    c = math.hypot(a,b)
    return c
print(main())
