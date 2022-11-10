#sorting a dictionary
result={'Raju':[45,67,89],'Gopal':[23,34,56]}
print("Initially the dictioary is:" + str(result))
sort_res=dict()
for key in sorted(result):
    sort_res[key]=sorted(result[key])
print("Dictionary after sorting is : ")
print(str(sort_res))