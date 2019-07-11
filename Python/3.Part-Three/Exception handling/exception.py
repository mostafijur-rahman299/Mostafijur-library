
def div(x,y):
    try:
        result=x/y
    except Exception as e:
        print("Error Happend: ",e)

div(2,0)
div('2',0)
