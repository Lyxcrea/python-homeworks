# Program Name: p17_Tuition_Table.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/21/18 - 9/22/18
# Description: Suppose that the tuition for a university is $10,000 this year
# and increases 5% every year. Write a program that computes the tuition in ten
# years and displays a table of the year and tution costs.

tuition = 10000
for year in range (1,11,1):
    print("Year %2i = " %year, "%2f" %tuition)
    tuition = tuition + tuition * .05


'''
>>> 
====== RESTART: C:\Users\Charlize\Documents\Python\p17_Tuition_Table.py ======
Year  1 =  10000.000000
Year  2 =  10500.000000
Year  3 =  11025.000000
Year  4 =  11576.250000
Year  5 =  12155.062500
Year  6 =  12762.815625
Year  7 =  13400.956406
Year  8 =  14071.004227
Year  9 =  14774.554438
Year 10 =  15513.282160
>>>
'''
