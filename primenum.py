print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):  # Start from 2, as 1 is not prime
    is_prime = True  # Assume the number is prime
    for i in range(2, num):  # Check divisors from 2 to (num - 1)
        if num % i == 0:  # If divisible, it's not prime
            is_prime = False
            break 
    if is_prime:
        print(num,end=" ")


# using function

# def is_prime(number):
#     if number <= 1:  # Numbers less than or equal to 1 are not prime
#         return False
#     for i in range(2, int(number**0.5) + 1):  # Check divisors from 2 to √number
#         if number % i == 0:
#             return False
#     return True

# # Display prime numbers from 1 to 100
# print("Prime numbers between 1 and 100 are:")
# for num in range(1, 101):
#     if is_prime(num):
#         print(num, end=" ")



        


       
        


    

