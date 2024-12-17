''' 15) Write a Python program to create a person class. Include attributes like name, country and date of
 birth. Implement a method to determine the person's age.'''

class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def age(self,present_year):
        self.age =present_year- self.dob
        
present_year = int(input('Enter the present year: '))
dob=int(input('Enter the date of birth: '))
name=input('Enter the name of the person: ')
country=input('Enter the country of the country: ')
a1=Person(name,country,dob)
age=a1.age(present_year)
print(a1.name)
print(a1.country)
print(a1.dob)
print(a1.age)
a2=Person(name,country,dob)
age=a2.age(present_year)
print(a1.name)
print(a2.country)
print(a2.dob)
print(a2.age)

