# Program Name: p21_Penny_or_Million_Dollars.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/21/18 - 9/22/18
# Description: Write a program which calculates exactly how much more (or less)
# you can make with the penny on day 30.

penny = 1

for day in range (1,31,1):
    print("Day %2i" %day, "%2i" %penny)
    penny = penny * 2
    if day == 30:
        dollar = penny/100
        print("On the 30th day, there are")
        print("{:,}".format(dollar), "dollars")

difference = dollar - 1000000

if dollar > 1000000:
    print("There are %f dollars more than $1,000,000 on day 1." %difference)
elif dollar < 1000000:
    print("There are %f dollars less than $1,000,000 on day 1." %difference)


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p21_Penny_or_Million_Dollars.py 
Day  1  1
Day  2  2
Day  3  4
Day  4  8
Day  5 16
Day  6 32
Day  7 64
Day  8 128
Day  9 256
Day 10 512
Day 11 1024
Day 12 2048
Day 13 4096
Day 14 8192
Day 15 16384
Day 16 32768
Day 17 65536
Day 18 131072
Day 19 262144
Day 20 524288
Day 21 1048576
Day 22 2097152
Day 23 4194304
Day 24 8388608
Day 25 16777216
Day 26 33554432
Day 27 67108864
Day 28 134217728
Day 29 268435456
Day 30 536870912
On the 30th day, there are
10,737,418.24 dollars
There are 9737418.240000 dollars more than $1,000,000 on day 1.
>>>
'''
