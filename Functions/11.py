#basic calculator
def cal(a,b):
    add = a + b
    subtract = a-b
    multiplication = a*b
    division = a / b
    return add, subtract , multiplication , division
one=int(input("Enter a number:"))
two=int(input("Enter another number:"))
output=cal(one , two)
print(output)