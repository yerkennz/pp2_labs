from math import tan, pi
n = int(input())
l = int(input())
area = n*l**2/(4*tan(pi/n))
print("The area of the polygon is:", int(area))