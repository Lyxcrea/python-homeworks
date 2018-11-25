# Program Name: p51_Classes_Assignment.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/16/18 - 11/17/18
# Description: 1) Create a Date class.
# 1a) The class should have 3 properties (instance variables):
# month
# day
# year
# 1b) The class should have 2 action (functions) :
# setDate()  - allows the user to enter a date in 12/31/02 format 
# showDate() - displays the date. 
# 2) Create an instance of the Date class.
# 3) Test the object's setDate() and showDate() methods.
# 4) Submit your program code, including the test run at the bottom of your
# code.


class Date:    
    
    def __init__(self, month = 11, day = 17, year = 18):
        self.month = month
        self.day = day
        self.year = year

    def setDate(self):
        fulldate = input("Please enter date in 12/31/02 format. ")
        lst = fulldate.split('/')
        self.month = lst[0]
        self.day = lst[1]
        self.year = lst[2]
    
    def showDate(self):        
        print(self.month + '/' + self.day + '/' + self.year)
        

aDate = Date()
aDate.setDate()
aDate.showDate()

'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p51_Classes_Assignment.py ===
Please enter date in 12/31/02 format. 11/17/18
11/17/18
>>>
'''
