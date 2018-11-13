# Program Name: p29_function_absoluteVal.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write the definition of, and test the function abs(num). The
# function returns the absolute value of a number.

def main():
    a = float(input("Enter a positive or negative value:"))
    if a >= 0:
        print("absolute value is:", a)
    if a < 0:
        a = a * (-1)
        print("absolute value is:", a)
main()

'''
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p29_function_absoluteVal.py 
Enter a positive or negative value:1
absolute value is: 1.0
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p29_function_absoluteVal.py 
Enter a positive or negative value:-1
absolute value is: 1.0
>>>
'''
