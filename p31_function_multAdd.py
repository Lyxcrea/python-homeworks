# Program Name: p31_function_multAdd.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write the definition of a function called multAdd. Write a main
# function which starts the program, and calls the multAdd function.

def multAdd(a,b,c):
    mult = a * b
    add = mult + c
    return add

def main():
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    num3 = int(input("Enter a number3: "))
    print(num1, " * ", num2, " + ", num3, " = ", multAdd(num1,num2,num3))

main()

'''
>>> 
==== RESTART: C:\Users\Charlize\Documents\Python\p31_function_multAdd.py ====
Enter a number1: 2
Enter a number2: 3
Enter a number3: 5
2  *  3  +  5  =  11
>>>
'''
