# x=float(input('Enter the percentage obtained:'))
# if x>=80:
#     print("Its distinction")
# elif x>=65:
#     print("First division")
# elif x>=55:
#     print("Second division")
# elif x>=40:  
#     print("Third division")
# else: x<40
# print("You failed")
       
def display(x):
    if x>=80:
        return "Distinction"
    elif x>=65:
        return "First division"
    elif x>=55:
        return "Second division"
    elif x>=40:
        return "Third division"
    
    else: return "You failed"

x=float(input('Enter percentage obtained: '))
result=display(x)
print(result)


    

