'''num=lambda x: 'Yes,the number given is even' if x%2==0 else 'No,the number given is not even,it is odd number'
print(num(3))
print(num(4))'''

# x = int(input('Enter the number: '))  
# if x % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

def odd_even(x):
     if x % 2 == 0:
          return 'Yes,the number is even'
     else:
          return 'The number is odd'
    
x=int(input('Enter the number: '))
result=odd_even(x)
print(result)
        
    




        
      
