# Program Name: myFunctions.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/11/18 - 11/11/18
# Description: Create a file myFunctions.py. Import that file/functions into
# another file (testFunctions.py) and then test/call all of them.

def min(list):
    low = list[0] 
    for i in list:
        if i < low:
            low = i
    return low


def max(list):
    high = list[0]
    for i in list:
        if i > high:
            high = i
    return high



def avg(list):
    total = 0
    for i in range(0, len(list), 1):
        total += list[i]
    return total / len(list)



def abs(num):
    if num < 0:
        return (num* -1)
    else:
        return (num* 1)


def find(key,list):
    found = 0
    for i in range (0, len(list), 1):
        if list[i] == key:
            found += 1
    if found == 0:
        return False
    else:
        return True



def isEven(number):
    if number%2 == 0:
        return True
    else:
        return False


