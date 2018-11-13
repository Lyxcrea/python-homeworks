# Program Name: p26_Count_Number_in_a_Random_List_of_Numbers.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a program that generates a random list of numbers.

from random import randint
X = randint(15,20)
count = 0

print('X =', X)
for number in range (0, X, 1):

    number = randint(2,5)
    print(number)

    if number == 3:
        count += 1
print("The number 3 occurs %i times." %count)


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p26_Count_Number_in_a_Random_List_of_Numbers.py 
X = 18
3
2
2
3
3
5
2
2
5
2
4
5
5
5
4
5
3
2
The number 3 occurs 4 times.
>>>
'''
