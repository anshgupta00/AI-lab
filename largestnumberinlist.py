# WAP program to get the largest number from a list.

lst=[]
n=int(input("enter how many number u want in the list:"))
print(n)

for i in range(1,n+1):
    num=int(input(f"enter the number{i}: "))
    lst.append(num)
print(lst)

largest = lst[0]
for x in lst:
    if x > largest:
        largest = x

print("The largest number in the list is:", largest)
print(max(lst))
    

