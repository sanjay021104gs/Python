def func(name , city , age ):
    print(name, city , age)
func("Sanjay","Hyderabad",17)

def func(*vals):
    for i in vals:
        print(i)
func(23,45,67,898,56,)