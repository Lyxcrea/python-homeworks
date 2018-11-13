# Program Name: p23_Arithmetic.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a program to let a child practice arithmetic skills.

from random import randint

repeat = 'y'

while repeat == 'y':
    
    num1 = randint(0,9)
    num2 = randint(0,9)
    
    operation = input("Would you like to add(+), sub(-) or mul(*): ")
    
    if operation == "+":
            answer = int(input("What is %i + %i = "%(num1,num2)))
            while answer != num1+num2:
                answer = int(input("Incorrect, what is %i + %i = "%(num1,num2)))
            else:
                print("Correct!")

    if operation == "-":
            answer = int(input("What is %i - %i = "%(num1,num2)))
            while answer != num1-num2:
                answer = int(input("Incorrect, what is %i - %i = "%(num1,num2)))
            else:
                print("Correct!")

    if operation == "*":
            answer = int(input("What is %i * %i = "%(num1,num2)))
            while answer != num1*num2:
                answer = int(input("Incorrect, what is %i * %i = "%(num1,num2)))
            else:
                print("Correct!")
                
    repeat = input("Would you like to try again(y/n): ")


'''
>>> 
======= RESTART: C:\Users\Charlize\Documents\Python\p23_Arithmetic.py =======
Would you like to add(+), sub(-) or mul(*): +
What is 8 + 6 = 3
Incorrect, what is 8 + 6 = 14
Correct!
Would you like to try again(y/n): y
Would you like to add(+), sub(-) or mul(*): +
What is 0 + 8 = 0
Incorrect, what is 0 + 8 = 8
Correct!
Would you like to try again(y/n): n
>>>
'''


