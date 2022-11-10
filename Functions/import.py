from re import L


total=0 #this is a global variable
def sum(x,y):
    total=x+y # this is a local variable
    print("inside function total:",total)
    return total;
sum(10,20) #function call
print("outside function total:",total)


#function without any parameters
def func():
    for i in range(5):
        print("yo wassup")
func()