# num=int(input("Enter any number: "))
def factorial(num):
    if num == 0 or num==1:
        return 1 #return is important to return the value to recursive funtion via base case
    else:
        return num*factorial(num-1)

#print(f"Factorial of {num} is:{factorial(num)}")

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")

table={}
def fiboM(num):
    if num==1 or num==2:
        return 1
    else:
        if num not in table:
            table[num] =fiboM(num-1)+fiboM(num-2)
        return table[num]

# tail cost optimization-get some knowledge of this
