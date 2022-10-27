#default argument example
def student(name, course , fees="10000"):
    print("name:",name)
    print("course:",course)
    print("fees:",fees)
n="Sanjay"
c="CSBS"
student(course=c,name=n)

#keyword argument example
def student(name, course , *fees):
    print("name:",name)
    print("course:",course)
    for f in fees:
        print("fees:",f)
student("Sanjay","CSBS","100","200","300")