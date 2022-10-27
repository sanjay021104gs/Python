#use of lambda functions
def myfunc(n):
    return lambda x : x * n
twice = myfunc(2)
print(twice(3))
thrice = myfunc(3)
print(thrice(3))
ft=myfunc(4)
print(ft(3))



#keyword argument
def student(name, fees , course):
    print("name:",name)
    print("course:",course)
    print("fees:",fees)
n="Sanjay"
c="CSBS"
f="20"
student(fees=f,course=c,name=n)