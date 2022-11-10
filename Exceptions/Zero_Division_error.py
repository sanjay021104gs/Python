x=int(input("enter the numerator:"))
y=int(input("enter the denominator:"))
try:
    res=x/y
    print("result:",res)
except ZeroDivisionError:
    print("denominator cannot be zero")