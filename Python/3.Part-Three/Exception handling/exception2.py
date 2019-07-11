def div(x,y):
    result=x/y
    return result

try:
    a=div(2,3)
except Exception as e:
    print("Error Happend: ",e)
else:
    print("Result is: ",a)
