# Program Name: p3_input.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started -  Date Finished: 8/30/18 - 8/30/18
# Description: Program to take input in Python

name = input ("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age =  int (input ("Please enter your age (whole number): " )) # an integer
weightKg = weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print (weightLbs, "lbs")
print ("which equals =%.2f" %weightKg, end=' ') # end='' prevents new line
print ("kilograms ")


'''
>>>
========== RESTART: C:\Users\Charlize\Documents\Python\p3_input.py ==========
Please enter Your Name: Charlize
Please enter Your weight in lbs: 118
Please enter your age (whole number): 13
Hello Human Charlize your weight is
118.0 lbs
which equals =53.52 kilograms 
>>>
'''
