# Program Name: p27_Count_Letters_in_a_Random_List_of_Letters.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a program that generates a random list of letters.

from random import randint

empty_list = []

x = randint(50, 75)
b_count = 0

print("Made a list of %i letters"%x)

for list in range(0, x, 1):
    letter_num = randint(65, 70)
    letter = chr(letter_num)
    if letter == 'B':
        b_count += 1
    empty_list.append(letter)

print(empty_list)
print("the letter 'B' appears %i times"%b_count)


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p27_Count_Letters_in_a_Random_List_of_Letters.py 
Made a list of 55 letters
['B', 'D', 'A', 'B', 'F', 'A', 'F', 'D', 'A', 'E', 'B', 'F', 'C', 'C', 'A', 'C', 'D', 'C', 'A', 'D', 'A', 'A', 'F', 'C', 'E', 'B', 'F', 'E', 'A', 'D', 'D', 'D', 'A', 'D', 'A', 'C', 'F', 'F', 'E', 'F', 'E', 'B', 'A', 'A', 'C', 'C', 'E', 'B', 'F', 'A', 'C', 'B', 'C', 'F', 'D']
the letter 'B' appears 7 times
>>>
'''
