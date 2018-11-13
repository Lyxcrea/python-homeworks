# Program Name: testFunctions.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/11/18 - 11/11/18
# Description: Create a file myFunctions.py. Import that file/functions into
# another file (testFunctions.py) and then test/call all of them.

import myFunctions
from myFunctions import min
from myFunctions import max
from myFunctions import avg
from myFunctions import abs
from myFunctions import find
from myFunctions import isEven

lst = [3, 5, 1, 10]
print("min: " + str(min(lst)))

print("max: " + str(max(lst)))

print("avg: " + str(avg(lst)))

val = -5
print("abs of " + str(val) + " is " + str(abs(val)))

key = 5
print("find " + str(key) + " in lst: " + str(find(key, lst)))

number = 5
print(str(number) + " is even: " + str(isEven(number)))


'''
>>> 
======== RESTART: C:\Users\Charlize\Documents\Python\testFunctions.py ========
min: 1
max: 10
avg: 4.75
abs of -5 is 5
find 5 in lst: True
5 is even: False
>>>
'''
