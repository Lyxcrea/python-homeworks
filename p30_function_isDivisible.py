# Program Name: p30_function_isDivisible.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write a function definition for function isDivisible that has two
# parameters, N and M.

def isDivisible(N, M):

    if N%M == 0:
        print(N, "is evenly divisible by", M)
    else:
        print(N, "is not evenly divisible by", M)


X = int(input("Enter an integer N: "))
Y = int(input("Enter an integer M: "))
print(isDivisible(X, Y))

'''
>>> 
== RESTART: C:\Users\Charlize\Documents\Python\p30_function_isDivisible.py ==
Enter an integer N: 4
Enter an integer M: 2
4 is evenly divisible by 2
>>> 
== RESTART: C:\Users\Charlize\Documents\Python\p30_function_isDivisible.py ==
Enter an integer N: 5
Enter an integer M: 2
5 is not evenly divisible by 2
>>>
'''
