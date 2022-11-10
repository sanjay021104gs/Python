try: 
    x=int(input("enter a positive integer"))
    if(x<0):
        raise ValueError("negative number input !")
except ValueError as e:
    print(e)