# WAP program to sum all the items in a list.

from functools import reduce

lst=[]

n=int(input(f"enter how many number you want in the list:"))
print(n)

for i in range(1,n+1):
    num = int(input(f"Enter number {i}: "))
    lst.append(num)

sum= reduce(lambda x,y:x+y,lst)
print("Sum of items is list is:",sum)
