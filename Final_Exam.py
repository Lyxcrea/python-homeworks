# Program Name: Final_Exam.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/23/18 - 11/24/18
# Description: A) Use a for loop to make 10 random numbers between 20 and 30
# and store them in a variable numList .
# ( Hint: use numList.append(number), where number is a randomint between 20
# and 30 )
# B) Sort the list. You may not use the sort(), sorted() or any other built-in
# python function!
# ( Hint: use 2 nested for loops as shown on class page )
# C) Show the sorted list and the unsorted list
# D) Find the sum, and average of the numbers in numList . You main not use
# sum() or average() python functions!
# ( Hint: use for loop)
# E) Find the median of the list.
# ( Hint for 10 numbers the median is the average of the two numbers in the
# middle)
# F) Show how many numbers are evenly divisible by 2
# G) Submit the Output of your program (A-F) as a multiline comment at the
# bottom of your program .

import random

numList = []

for i in range(0, 10, 1):    
    number = random.randint(20,30)
    numList.append(number)

def mySort(list):
    for j in range (0, len(list), 1): 
        for i in range (0, len(list)-1, 1): 
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1] 
                list[i+1] = temp
    return list

sortList = []
for i in numList:
    sortList.append(int(i))

sortList = mySort(sortList)

print("Original List:", numList)
print("Sorted List:", sortList)

def sum(list):
    total = 0
    for i in range(0,len(list), 1):
        total += list[i]
    return total

print("Sum of list is", sum(numList))

def average(list):
    total = 0
    for i in range(0, len(list), 1):
        total += list[i]
    return total / len(list)

print("Average of list is", average(numList))

def calcMedian(list):
    median = 0
    middle = int(len(list) / 2)
    if (len(list) % 2 == 0):
        median = (list[middle - 1] + list[middle]) / 2
    else:
        median = list[middle] 
    return median

print("Median of list is", calcMedian(numList))


evencnt = 0
def isEven(N):
    if N%2 == 0:
        return True
    else:
        return False

for i in numList:
    if isEven(i):
        evencnt += 1

print("There are %s numbers even." %evencnt)


'''
>>> 
========= RESTART: C:\Users\Charlize\Documents\Python\Final_Exam.py =========
Original List: [23, 26, 26, 21, 27, 24, 26, 27, 22, 28]
Sorted List: [21, 22, 23, 24, 26, 26, 26, 27, 27, 28]
Sum of list is 250
Average of list is 25.0
Median of list is 25.5
There are 6 numbers even.
>>>
'''


