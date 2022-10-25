result = {
    'Rahul': [45,67],
    'Rupesh':[89,90],
    'Rakesh':[88,34],
    'Rohith':[56,76],
}
total=0
final=result.copy()
total=0
final=result.copy()
for key,val in result.items():
    total=sum(val)
    final[key]=total
    print(final)
hig=0
Topper=''
for key , val in final.items():
    if val>hig:
        hig=val
        Topper=key
print("Topper is :", Topper ,"securing",   hig , "marks")