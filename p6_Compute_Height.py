# Program Name: p6_Compute_Height.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/2/18 - 9/2/18
# Description: Write a program to compute a person's height.

# ask the user for height, feet and inches
print("Please enter your height.")
feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))
# calculate the total inches
total_inches = feet * 12 + inches
# show the results
print("%.0f feet + %.0f inches = %.0f inches" %(feet, inches, total_inches))


'''
>>> 
====== RESTART: C:\Users\Charlize\Documents\Python\p6_Compute_Height.py ======
Please enter your height.
Enter the number of feet: 4
Enter the number of inches: 10
4 feet + 10 inches = 58 inches
>>>
'''
