# Program Name: p33_function_isEven.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write a function named isEven that takes an integer N and returns
# true if N is even.

def isEven(N):
    if N%2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if isEven(num):
    print("Your number is even")
else:
    print("Your number is odd")

'''
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p33_function_isEven.py =====
Enter a number: 3
Your number is odd
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p33_function_isEven.py =====
Enter a number: 4
Your number is even
>>>
'''
