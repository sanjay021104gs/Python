try:
    x=int(input("enter a number:"))
    y=x+2
    print("y=",y)
except(KeyboardInterrupt,ValueError):
    print("enter the number again")
