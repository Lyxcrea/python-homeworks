# Program Name: p28_function_sumDouble_SHOW_vs_RETURN.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/6/18 - 10/6/18
# Description: Write a function sum_double(a,b) which given two integer
# parameters RETURNS their sum.

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    return a + b

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
z = sum_double(x, y)
print(z)

'''
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p28_function_sumDouble_SHOW_vs_RETURN.py 
Enter number x: 1
Enter number y: 2
3
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p28_function_sumDouble_SHOW_vs_RETURN.py 
Enter number x: 3
Enter number y: 2
5
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p28_function_sumDouble_SHOW_vs_RETURN.py 
Enter number x: 2
Enter number y: 2
8
>>> 
 RESTART: C:\Users\Charlize\AppData\Local\Programs\Python\Python37-32\p28_function_sumDouble_SHOW_vs_RETURN.py 
Enter number x: 3
Enter number y: 3
12
>>>
'''
