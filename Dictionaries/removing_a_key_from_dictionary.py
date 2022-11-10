#removing a key from dictionary
name={'Ashok':35,'Ravi':23,'Sundar':17}
print("the dictionary is :",name)
delete=input("Enter the key which you want to delete: ")
del name[delete]
print("the dictionary after the key deleted is:",name)
