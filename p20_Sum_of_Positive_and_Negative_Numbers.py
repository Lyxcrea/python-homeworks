# Program Name: p20_Sum_of_Positive_and_Negative_Numbers.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/21/18 - 9/22/18
# Description: Write a program that reads in X whole numbers and outputs (1) the
# sum of all positive numbers, (2) the sum of all negative numbers, and (3) the
# sum of all positive and negative numbers. The user can enter the X numbers in
# any different order every time, and can repeat the program if desired.

loop = 'y'

while loop == 'y' or loop == 'yes':
    
    X = int(input("How many numbers would you like to enter?"))

    Sum = 0
    SumNeg = 0
    SumPos = 0
    for index in range (0,X,1):
        number = float(input("Enter number %i " %(index+1) ))
        Sum += number

        if number < 0:
            SumNeg += number
        if number > 0:
            SumPos += number
            
    print("SumNeg: ", SumNeg)
    print("SumPos: ", SumPos)
    print("Sum: ", Sum)

    loop = input("Would you like to repeat? (y)(n): ")
    

'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p20_Sum_of_Positive_and_Negative_Numbers.py 
How many numbers would you like to enter?4
Enter number 1 3
Enter number 2 -4
Enter number 3 -6
Enter number 4 5
SumNeg:  -10.0
SumPos:  8.0
Sum:  -2.0
Would you like to repeat? (y)(n): n
>>>
'''
