mtocm={ m : m * 100 for m in range(1,11)}
print("metres to centimetres:" ,mtocm)



cubes={c : c ** 3 for c in range(1,10) if c % 2 == 1}
print("cube root is ", cubes)



def cnt(msg):
    lc={}
    for l in msg:
        lc[l]=lc.get(l,0)+1
    print(lc)
msg=input("enter a messaage:")
cnt(msg)