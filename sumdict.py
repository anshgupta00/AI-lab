# 12)WAP to find the sum of all items in a dictionary
# Input: {'a': 100, 'b':200, 'c':300}
#  Output: 600
#  Input: {'x': 25, 'y':18, 'z':45}
#  Output: 88


#Function to calculate the sum of all values in a dictionary
def sum_of_dict_values(dictionary):
    return sum(dictionary.values())

#Example 1
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(f"Input: {dict1}")
print(f"Output: {sum_of_dict_values(dict1)}")

#Example 2
dict2 = {'x': 25, 'y': 18, 'z': 45}
print(f"\nInput: {dict2}")
print(f"Output: {sum_of_dict_values(dict2)}")




# Calculate the sum of all values in a dictionary without using sum()
def sum_of_dict_values(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Example 1
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(f"\nInput: {dict1}")
print(f"Output: {sum_of_dict_values(dict1)}")

# Example 2
dict2 = {'x': 25, 'y': 18, 'z': 45}
print(f"\nInput: {dict2}")
print(f"Output: {sum_of_dict_values(dict2)}")


