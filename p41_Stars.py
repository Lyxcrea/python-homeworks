# Program Name: p41_Stars.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write a function which outputs as many crosses as the parameter
# 'numCrosses' indicates.

numstars = int(input("Enter how many stars: "))
 
def stars(numCrosses):
    for x in range(1, numCrosses + 1, 1):        
        for y in range(0, x, 1):            
            print("+", end='')
        print("")

stars(numstars)

'''
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p41_Stars.py ==========
Enter how many stars: 5
+
++
+++
++++
+++++
>>>
'''
