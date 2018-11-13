# Program Name: p43_sort(list,reverse)_function.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write the following python function 
# def sort(list, reverse)
# The function returns the sorted list in ascending order if parameter 'reverse'
# is False
# The function returns the sorted list in descending order if parameter
# 'reverse' is True

def sort(list, reverse):
    if reverse == False:
        for j in range (0, len(list), 1): 
          for i in range (0, len(list)-1, 1): 
            if list[i] > list[i+1]:
              temp = list[i]
              list[i] = list[i+1] 
              list[i+1] = temp
    if reverse == True:
        for j in range (0, len(list), 1): 
          for i in range (0, len(list)-1, 1): 
            if list[i] < list[i+1]:
              temp = list[i]
              list[i] = list[i+1] 
              list[i+1] = temp
        
    return list

list = [5,1,4,3,2]
print(sort(list, False))
print(sort(list, True))

'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p43_sort(list,reverse)_function.py 
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
>>>
'''
