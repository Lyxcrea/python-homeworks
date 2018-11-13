# Program Name: p15_Sum_of_Positive_Negative_All.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/9/18 - 9/9/18
# Description: Write a program that asks the user to enter 4 numbers
# (positive or negative).

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a number: "))
num3 = float(input("Please enter a number: "))
num4 = float(input("Please enter a number: "))

sumNeg = 0
sumPos = 0

if num1 < 0:
    sumNeg += num1
else:
    sumPos += num1
if num2 < 0:
    sumNeg += num2
else:
    sumPos += num2
if num3 < 0:
    sumNeg += num3
else:
    sumPos += num3
if num4 < 0:
    sumNeg += num4
else:
    sumPos += num4
    
print("Sum of all negative numbers: %i" %sumNeg)
print("Sum of all positive numbers: %i" %sumPos)

sumAll = num1 + num2 + num3 + num4

print("Sum of all numbers: %i" %sumAll)


'''
>>> 
 RESTART: C:/Users/Charlize/Documents/Python/p15_Sum_of_Positive_Negative_All.py 
Please enter a number: 1
Please enter a number: 2
Please enter a number: 3
Please enter a number: 4
Sum of all negative numbers: 0
Sum of all positive numbers: 10
Sum of all numbers: 10
>>> 
 RESTART: C:/Users/Charlize/Documents/Python/p15_Sum_of_Positive_Negative_All.py 
Please enter a number: -5
Please enter a number: -5
Please enter a number: 6
Please enter a number: 4
Sum of all negative numbers: -10
Sum of all positive numbers: 10
Sum of all numbers: 0
>>>
'''
