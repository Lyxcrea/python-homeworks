# Program Name: p42_sum()_average()_min()_max().py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write the definitions for the following 4 functions:
# 1. sum (list_parameter) : returns the sum of numbers inside a list
# 2. average (list_parameter) : returns the average of numbers inside a list
# 3. min (list_parameter) : returns the smallest of all numbers inside a list
# 4. max (list_parameter) : returns the largest of all numbers inside a list
# 5. main () : calls all the other functions

def sum(myList):
    total = 0
    for i in range(0,len(myList), 1):
        total += myList[i]
    return total

def average(myList):
    total = 0
    for i in range(0, len(myList), 1):
        total += myList[i]
    return total / len(myList)

def min(myList):
    lowest = myList[0]
    for i in range(0, len(myList), 1):
        if myList[i] < lowest:
            lowest = myList[i]
    return lowest

def max(myList):
    highest = myList[0]
    for i in range(0, len(myList), 1):
        if myList[i] > highest:
            highest = myList[i]
    return highest

def main():
    aList = [1,2,3]
    s = sum(aList)
    print("The sum of numbers inside the list", aList, "is:", s)
    s = average(aList)
    print("The average of numbers inside the list", aList, "is:", s)
    s = min(aList)
    print("The min of numbers inside the list", aList, "is:", s)
    s = max(aList)
    print("The max of numbers inside the list", aList, "is:", s)
    

main()


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p42_sum()_average()_min()_max().py 
The sum of numbers inside the list [1, 2, 3] is: 6
The average of numbers inside the list [1, 2, 3] is: 2.0
The min of numbers inside the list [1, 2, 3] is: 1
The max of numbers inside the list [1, 2, 3] is: 3
>>>
'''

