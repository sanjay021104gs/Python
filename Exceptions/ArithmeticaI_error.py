try:
    num1=int(input("enter the first value "))
    num2=int(input("enter the second value"))
    if (num2==0):
        raise ArithmeticError
    else:
        print("result=",num1/num2)
except ArithmeticError:
    print("numd2 cannot be zero")
#try means
#this next block of code might throw some exceptions

#catch means
#if my listed exception happens, then run this block of code in response so I can maybe fix things. Follow the inheritance tree of exception superclasses if it’s not the exact one I mean

#finally means
#whatever just happened or didn’t happen, run this code at the very end. Give me a chance to clean up after myself