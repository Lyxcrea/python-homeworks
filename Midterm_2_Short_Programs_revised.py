# Program Name: Midterm_2_Short_Programs_revised.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/28/18 - 10/28/18
# Description: Function 1: Write a function which takes 2 float PARAMETERS
# distance and time. The functions computes and SHOWS the speed = distance/time
# rounded to 2 values to the right of the decimal point.
# Function 2: Write a function which takes 3 integer PARAMETERS num1, num2,
# num3. The function then RETURNS the middle/median value of the 3 arguments.
# Assume 3 different values as parameters.

import random

def sort(lst):
    for j in range (0, len(lst), 1): 
        for i in range (0, len(lst)-1, 1): 
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1] 
                lst[i+1] = temp        
    return lst

def function1(distance, time):
    speed = distance/time
    print("Distance: %.2f / Time: %.2f = Speed: %.2f" %(distance, time, speed))

distance = random.uniform(0,1000.0)
time = random.uniform(0,100.0)   
function1(distance, time)

def function2(num1, num2, num3):
    lst = [num1, num2, num3]
    sortlst = sort(lst)
    middle = sortlst[1]
    print("Middle of [%i,%i,%i] = %i" %(num1, num2, num3, middle))


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
function2(num1, num2, num3)


'''
>>> 
 RESTART: C:/Users/Charlize/Documents/Python/Midterm_2_Short_Programs_revised.py 
Distance: 713.83 / Time: 4.59 = Speed: 155.35
Middle of [3,1,8] = 3
>>> 
'''
    
