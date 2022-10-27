total=0 #this is a global variable
def sum(x,y):
    total=x+y # this is a local variable
    print("inside function total:",total)
    return total;
sum(10,20) #function call
print("outside function total:",total)
