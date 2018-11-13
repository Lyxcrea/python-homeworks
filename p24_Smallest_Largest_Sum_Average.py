# Program Name: p24_Smallest_Largest_Sum_Average.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a program that generates X random integers Num.

from random import randint

X = randint(10,15)

print( 'x =', X)
sum = 0
for i in range (0, X, 1):

    number = randint(20,50)
    sum += number
    print(number)

    if i == 0:
        smallest = number
        largest = number 

    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

print('smallest =', smallest)
print('largest =', largest)
print('sum = ', sum)
print('avg =', sum/X)


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p24_Smallest_Largest_Sum_Average.py
x = 15
22
37
40
39
45
20
45
40
33
32
21
36
28
27
21
smallest = 20
largest = 45
sum =  486
avg = 32.4
>>>
'''
