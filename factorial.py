#WAP to calculate the factorial of an input number


num=int(input("Enter any number: "))
def factorial(num):
    if num == 0 or num==1:
        return 1 #return is important to return the value to recursive funtion via base case
    else:
        return num*factorial(num-1)

#print(f"Factorial of {num} is:{factorial(num)}")

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")
   
 
 