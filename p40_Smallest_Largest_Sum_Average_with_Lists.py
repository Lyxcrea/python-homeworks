# Program Name: p40_Smallest_Largest_Sum_Average_with_Lists.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: 1) Ask the user to enter X numbers into a list. 2) Put those
# numbers into a list, and show the list. 3) Calculate and show the sum,
# average, min, max of those numbers. 4) You are not allowed to use any
# pre-existing python functions such as sample(), sum(), min(), max(),
# average(), sort(), sorted()!!!...unless you write them yourself. 5) Now make
# another list, but with double the values of the first list.

X = int(input("How many numbers would you like to enter? "))
listTemp = []

for i in range(0, X, 1):
    ix = str(i + 1) + ": "
    n = int(input("Enter number " + ix))
    listTemp.append(n)

print(listTemp)

total = 0
for i in listTemp:
    total += i
    
print("Sum = ", total)

print("Average =", total, "/", X, "= ", total/X)

smallest = listTemp[0]
for i in listTemp:
    if i < smallest:
        smallest = i
        
print("Smallest = ", smallest)

largest = listTemp[0]
for i in listTemp:
    if i > largest:
        largest = i
        
print("Largest = ", largest)

list2 = []
for i in listTemp:
    list2.append(i * 2)

print("List 2: ", list2)

'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p40_Smallest_Largest_Sum_Average_with_Lists.py 
How many numbers would you like to enter? 11
Enter number 1: 26
Enter number 2: 23
Enter number 3: 48
Enter number 4: 32
Enter number 5: 44
Enter number 6: 21
Enter number 7: 32
Enter number 8: 20
Enter number 9: 49
Enter number 10: 48
Enter number 11: 34
[26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34]
Sum =  377
Average = 377 / 11 =  34.27272727272727
Smallest =  20
Largest =  49
List 2:  [52, 46, 96, 64, 88, 42, 64, 40, 98, 96, 68]
>>>
'''
