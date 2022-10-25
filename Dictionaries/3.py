#To get minimum and maximum mark
dict={
    'Maths': 98,
    'Science': 89,
    'English': 78,
    'Social': 90,
}
print('Maximum mark is :' , max(dict,key=dict.get))
print('Minimum mark is :', min(dict,key=dict.get))