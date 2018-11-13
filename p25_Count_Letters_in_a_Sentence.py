# Program Name: p25_Count_Letters_in_a_Sentence.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a program that asks the user to input a sentence.

sentence = input("Please enter a sentence: ")
letter1 = input("Please enter letter 1: ")
letter2 = input("Please enter letter 2: ")
count1 = 0
count2 = 0
for i in range (0,len(sentence), 1):
    if sentence[i] == letter1:
        count1 += 1
    if sentence[i] == letter2:
        count2 += 1
print("The letter", letter1, "was found", count1, "times.")
print("The letter", letter2, "was found", count2, "times.")


'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p25_Count_Letters_in_a_Sentence.py 
Please enter a sentence: HELLO WORLD
Please enter letter 1: O
Please enter letter 2: L
The letter O was found 2 times.
The letter L was found 3 times.
>>>
'''
