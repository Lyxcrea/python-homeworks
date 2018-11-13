# Program Name: p32_function_isTriangle.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write a function named isTriangle(a,b,c) that takes three sides
# a,b,c as arguments, and returns either True or False, depending on whether you
# can form a triangle from the sides with the given lengths.

def isTriangle(a,b,c):
    if a + b < c:
        return False
    elif b + c < a:
        return False
    elif c + a < b:
        return False
    else:
        return True
    
stick1 = int(input("Enter length of stick1 (inches): "))
stick2 = int(input("Enter length of stick2 (inches): "))
stick3 = int(input("Enter length of stick3 (inches): "))
if isTriangle(stick1, stick2, stick3):
    print("The 3 sticks can form a triangle")
else:
    print("The 3 sticks cannot form a triangle")

'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p32_function_isTriangle.py ===
Enter length of stick1 (inches): 3
Enter length of stick2 (inches): 4
Enter length of stick3 (inches): 12
The 3 sticks cannot form a triangle
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p32_function_isTriangle.py ===
Enter length of stick1 (inches): 2
Enter length of stick2 (inches): 4
Enter length of stick3 (inches): 6
The 3 sticks can form a triangle
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p32_function_isTriangle.py ===
Enter length of stick1 (inches): 4
Enter length of stick2 (inches): 7
Enter length of stick3 (inches): 10
The 3 sticks can form a triangle
>>>
'''
