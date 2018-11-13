# Program Name: p10_Letter_Grades.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/2/18 - 9/2/18
# Description: Write a program which asks the user for a student's grade as a
# percent, and then returns their letter grade.

percent = float(input("Enter your grade percentage. "))

if percent < 0 or percent >100:
    print("ERROR, enter a grade percent between 0-100")
    percent = float(input("Enter your grade percentage. "))

if percent >= 90 and percent <=100:
    print("Your grade is an 'A'")

if percent >=  80 and percent < 90:
    print("Your grade is a 'B'")

if percent >= 70 and percent < 80:
    print("Your grade is a 'C'")

if percent >= 60 and percent <70:
    print("Your grade is a 'D'")

if percent < 60:
    print("Your grade is an 'F'")


'''
>>> 
====== RESTART: C:/Users/Charlize/Documents/Python/p10_Letter_Grades.py ======
Enter your grade percentage. -1
ERROR, enter a grade percent between 0-100
Enter your grade percentage. 75
Your grade is a 'C'
>>>
'''
