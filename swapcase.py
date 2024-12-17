# 13) You are given a string and your task is to swap cases. In other words, convert all lowercase letters 
# to uppercase letters and vice versa.


def swap_case(s):
    return s.swapcase()


# input_string = "Hello World"
input_string =input("Enter any string to swap: ")
result = swap_case(input_string)
print(result)  
