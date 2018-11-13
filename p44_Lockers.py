# Program Name: p44_Lockers.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write a program to determine which exact locker numbers are open,
# and total number that are open.

lockers = []
numlockers = 1000

for i in range(0, numlockers, 1):
    lockers.append(1)

for s in range(0, numlockers, 1):
    for i in range(s, numlockers, s+1):
        if lockers[i] == 1:
            lockers[i] = 0
        else:
            lockers[i] = 1    

count = 0
for i in range(0, numlockers, 1):
    if lockers[i] == 0:
        print("Locker #", i + 1, "is open")
        count += 1
        
print("Total number of lockers: ", numlockers)
print("Number of lockers that are open: ", count)


'''
>>> 
========= RESTART: C:\Users\Charlize\Documents\Python\p44_Lockers.py =========
Locker # 1 is open
Locker # 4 is open
Locker # 9 is open
Locker # 16 is open
Locker # 25 is open
Locker # 36 is open
Locker # 49 is open
Locker # 64 is open
Locker # 81 is open
Locker # 100 is open
Locker # 121 is open
Locker # 144 is open
Locker # 169 is open
Locker # 196 is open
Locker # 225 is open
Locker # 256 is open
Locker # 289 is open
Locker # 324 is open
Locker # 361 is open
Locker # 400 is open
Locker # 441 is open
Locker # 484 is open
Locker # 529 is open
Locker # 576 is open
Locker # 625 is open
Locker # 676 is open
Locker # 729 is open
Locker # 784 is open
Locker # 841 is open
Locker # 900 is open
Locker # 961 is open
Total number of lockers:  1000
Number of lockers that are open:  31
>>>
'''
