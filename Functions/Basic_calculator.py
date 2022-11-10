from __future__ import division


#basic calculator
def cal(a,b):
    add = a + b
    subtract = a-b
    multiplication = a*b
    division = a / b
    return add, subtract , multiplication , division
output=cal(23,7)
print(output)