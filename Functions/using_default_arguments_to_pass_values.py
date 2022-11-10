#using default argument to pass values

def disp(name, course = 'MCA'):
    print('Name:' + name)
    print('course:'+course)

disp(course='BCA',name = 'Bolu')
disp(name='Gokul')



#adding two numbers using lambda function
sum=lambda a , b : a + b
print("Sum=" ,sum(23,44))


#check whether two numbers are equal or not

def num(x,y):
    if(x==y):
        return 0
    if(x>y):
        return 1
    if(x<y):
        return -1
check = num(3,50)
if(check==0):
    print('x and y are equal')
if (check==1):
    print("x is greater than y")
if (check==-1):
    print("y is greater than x")