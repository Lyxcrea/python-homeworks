# Program Name: p13_Coin_Conversion.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/8/18 - 9/8/18
# Description: Write a program to convert any given number of total cents
# (under 100) into the correct number of: quarters, dimes, nickels, pennies.

totalCents = int(input("Please enter total cents: "))

q = int(totalCents/25)
if q > 0:
    print("you have", q, "quarters")
    totalCents = totalCents - q*25

d = int(totalCents/10)
if d > 0:
    print("you have", d, "dimes")
    totalCents = totalCents - d*10

n = int(totalCents/5)
if n > 0:
    print("you have", n, "nickels")
    totalCents = totalCents - n*5

p = int(totalCents/1)
if p > 0:
    print("you have", p, "pennies")
    totalCents = totalCents - p*1


'''
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p13_Coin_Conversion.py =====
Please enter total cents: 66
you have 2 quarters
you have 1 dimes
you have 1 nickels
you have 1 pennies
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p13_Coin_Conversion.py =====
Please enter total cents: 16
you have 1 dimes
you have 1 nickels
you have 1 pennies
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p13_Coin_Conversion.py =====
Please enter total cents: 6
you have 1 nickels
you have 1 pennies
>>> 
===== RESTART: C:\Users\Charlize\Documents\Python\p13_Coin_Conversion.py =====
Please enter total cents: 4
you have 4 pennies
>>>
'''
