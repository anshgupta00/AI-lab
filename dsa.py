import recursion

num=int(input("Enter any number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {recursion.factorial(num)}")

if num<0:
    print("Fibonacci series is not defined for negative numbers")
else:
    print(f"Fibonacci of {num}th term is {recursion.fiboM(num)}")