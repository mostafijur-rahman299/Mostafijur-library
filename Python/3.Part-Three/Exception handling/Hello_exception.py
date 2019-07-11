
def div(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Cann't divide by zero")
        return None

    except TypeError:
        print("String type can't accepted")
        return None

    return result


print(div('9',3))
print(div(9,0))


###########################
