''' 14) Write a Python program to create a class representing a Circle. Include methods to calculate its area
 and perimeter.'''

# import math
from math import*

class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.area=0
        self.perimeter=0
    def calc(self):
        self.area = pi*self.radius*self.radius
        self.perimeter = 2*pi*self.radius

r=int(input("enter the radius of cirlce: "))

   #create a circle object     
c=Circle(r)
c.calc()

print(f"Area of circle is: ",c.area)
print(f"Perimeter of circle is: ",c.perimeter)
    