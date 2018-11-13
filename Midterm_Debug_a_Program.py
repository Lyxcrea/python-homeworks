# Program Name: Midterm_Debug_a_Program.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/27/18 - 10/27/18
# Description: Debug/fix the following program so that it shows the indicated
# output.

num = int(input("Please enter a number: "))

def isEven(num): 
  if (num%2 == 0):
     return True
  elif (num%2 != 0):
     return False

def main():
   print("The number %i is even: %s" %(num, isEven(num)))
main()


'''
>>> 
=== RESTART: C:/Users/Charlize/Documents/Python/Midterm_Debug_a_Program.py ===
Please enter a number: 5
The number 5 is even: False
>>>
'''
