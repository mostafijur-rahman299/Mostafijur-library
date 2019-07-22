class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    # Operator overloading
    def __add__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        return s1 + s2
        
    
s1 = Student(34,53)
s2 = Student(32, 78)
result = s1 + s2

####################################################################

class Student2:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False
        
s1 = Student2(36, 87)
s2 = Student2(68, 23)

if s1 > s2:
    print("Win's")
else:
    print('Lose')
