# Program Name: p9_User_Height_Message.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/2/18 - 9/2/18
# Description: Write a program to compute a person's height and print out a
# message.

print("Enter your height.")
feet = int(input("feet: "))
inches = int(input("inches: "))
total= feet * 12 + inches
if total > 72:
    print("You are tall.")
if total >= 60 and total <= 72:
    print("You are average.")
if total < 60:
    print("You are vertically challenged.")


'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p9_User_Height_Message.py ===
Enter your height.
feet: 4
inches: 11
You are vertically challenged.
>>>
'''
