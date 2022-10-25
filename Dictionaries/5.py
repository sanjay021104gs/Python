#get method
car= {
    "model" : "alto",
    "year"  : 2010,
    "brand" : "maruti"
}
print(car.get("model"))

#to print the sum of key value 
dict= {1:34,2:29,3:49}
sumval=[]
for keys in dict:
    sumval.append(keys+dict[keys])
print("key value sum is",sumval)


#program for handling the missing keys in dictionary using get method
names={'sharma':'CEO','Saikia':'Manager','Ali':'Executive'}
search_key= input("enter the key to be searched:")
print(names.get(search_key,"search key not present"))


#using == operator
emp1={"id":101,"name":"sanjay","age":17}
emp2={"id":101,"name":"sanjay","age":17}
emp3={"id":102,"name":"kishore","age":18}
if emp1==emp2:
    print("emp 1 and emp 2 are same dictionaries")
else:
    print("emp 1 and emp 2 are not same dictionaries")
if emp2==emp3:
    print("emp 2 and emp 3 are same dictionaries")
else:
    print("emp 2 and emp 3 are not same dictionaries")