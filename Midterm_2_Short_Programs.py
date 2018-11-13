# Program Name: Midterm_2_Short_Programs.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/27/18 - 10/27/18
# Description: Function 1: Write a function which takes 2 float PARAMETERS
# distance and time. The functions computes and SHOWS the speed = distance/time
# rounded to 2 values to the right of the decimal point.
# Function 2: Write a function which takes 3 integer PARAMETERS num1, num2,
# num3. The function then RETURNS the middle/median value of the 3 arguments.
# Assume 3 different values as parameters.

import statistics
import random

def function1(distance, time):
    speed = distance/time
    print("Distance: %.2f / Time: %.2f = Speed: %.2f" %(distance, time, speed))

distance = random.uniform(0,1000.0)
time = random.uniform(0,100.0)   
function1(distance, time)

def function2(num1, num2, num3):
    middle = statistics.median([num1, num2, num3])
    print("Middle of [%i,%i,%i] = %i" %(num1, num2, num3, middle))

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
num3 = random.randint(0, 10)
function2(num1, num2, num3)


'''
>>> 
== RESTART: C:/Users/Charlize/Documents/Python/Midterm_2_Short_Programs.py ==
Distance: 854.80 / Time: 7.01 = Speed: 121.97
Middle of [7,3,4] = 4
>>>
'''
    
