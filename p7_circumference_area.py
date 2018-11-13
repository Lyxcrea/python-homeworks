# Program Name: p7_circumference_area.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/2/18 - 9/3/18
# Description: Write a program to compute the circumference and area of a
# circle.

PI = 3.1415
radius = float(input("Enter the radius (in inches). "))
area = PI * radius * radius
circumference = 2 * PI * radius

print("A circle with radius %.1f inches has" %radius)
print("circumference: %.1f inches" %circumference)
print("area: %.1f square inches" %area)


'''
>>> 
==== RESTART: C:\Users\Charlize\Documents\Python\p7_circumference_area.py ====
Enter the radius (in inches). 12
A circle with radius 12.0 inches has
circumference: 75.4 inches
area: 452.4 square inches
>>>
'''
