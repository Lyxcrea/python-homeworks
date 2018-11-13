# Program Name: p45_Prime_Numbers.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write a program that calculates and shows all prime numbers
# between 3 - 100.Prime numbers can only be evenly (remainder 0) divided by
# itself and 1.

for n in range(3, 101, 1):
    for j in range(2, n + 1, 1):
        if n % j == 0 and n != j:
            break
        elif n % j == 0 and n == j:
            print(n)
            break
        

'''
>>> 
====== RESTART: C:\Users\Charlize\Documents\Python\p45_Prime_Numbers.py ======
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>>
'''
