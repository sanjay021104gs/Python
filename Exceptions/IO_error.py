try:
    x=open('newfile.txt')
    s=x.readline()
    print(s)
except(IOError):
    print("input error")
except:
    print("error occured program terminated")
else:
    print("program runned successfully")