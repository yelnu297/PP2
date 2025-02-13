import math
a=int(input("Input number of sides: "))
b=int(input("Input side length: "))
print("Area of a regular polygon: ", (a*b**2)/(4*math.tan(math.pi/a)))  