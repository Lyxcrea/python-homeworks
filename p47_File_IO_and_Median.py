# Program Name: p47_File_IO_and_Median.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/3/18 - 11/3/18
# Description: 3) Write a program which 
# a) Writes a random number (50 to 55) of numbers (0 - 100) in a file
# b) Opens the file and reads the numbers from it into a list
# c) Sorts the list and Shows it. (you can't use python built-in functions
# sort(), sorted(), sum(), must write your own code)
# d) Calculates the median (can't use any python built-in function for median)

import random

def mySort(list):
    for j in range (0, len(list), 1): 
        for i in range (0, len(list)-1, 1): 
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1] 
                list[i+1] = temp
    return list

def calcMedian(list):
    median = 0
    middle = int(len(list) / 2)
    if (len(list) % 2 == 0):
        print("List has even total numbers.")
        median = (list[middle - 1] + list[middle]) / 2
    else:
        print("List has odd total numbers.")
        median = list[middle] 
    return median
            
myFile = open('randomNumbers.txt', 'w')
totalnumber = random.randint(0, 100)

for i in range (0, totalnumber, 1):
    number = random.randint(50, 55)
    myFile.write(str(number) + '\n')

myFile.close()

myFile = open('randomNumbers.txt', 'r')
myList = myFile.read().splitlines()

myFile.close()

sortList = []
for i in myList:
    sortList.append(int(i))
print("Original List... ")
print(sortList)
print()

sortList = mySort(sortList)

print("Sorted List...")
print(sortList)
print()

print("Median of list is ", calcMedian(sortList))


'''
>>> 
=== RESTART: C:/Users/Charlize/Documents/Python/p47_File_IO_and_Median.py ===
Original List... 
[53, 55, 54, 55, 53, 52, 51, 52, 54, 55, 50, 55, 54, 52, 54, 51, 53, 54, 53, 51, 51, 53, 50, 51, 50, 52, 55, 50, 55, 54, 53, 53, 50, 53, 52, 51, 53, 53, 53, 53, 54, 53, 50, 54, 50, 50, 53, 55, 54, 50, 55, 52, 50, 51, 50, 52, 54, 54, 52, 53, 53]

Sorted List...
[50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55]

List has odd total numbers.
Median of list is  53
>>>
=== RESTART: C:/Users/Charlize/Documents/Python/p47_File_IO_and_Median.py ===
Original List... 
[55, 50, 50, 54, 53, 53, 52, 52, 55, 51, 52, 53, 52, 53, 52, 54, 54, 52, 53, 52, 51, 52, 55, 52, 52, 50, 50, 53, 54, 52]

Sorted List...
[50, 50, 50, 50, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55]

List has even total numbers.
Median of list is  52.0
>>>
'''

