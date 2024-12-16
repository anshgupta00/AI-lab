'''calc=lambda a,b:(a+b,a-b,a*b,a / b)
#
print(calc(3,2))'''

#
'''
def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
print(calc(4,2))'''

lst=[int(x) for x in input("enter any two numbers:").split()]
def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
print(lst)
print(calc(lst[0],lst[1]))



