# Program Name: p38_Find_Longest_Word.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write a program that asks the user to enter a sentence. The
# program then finds the longest word in the sentence, and shows it.

sentence = input("Please enter a sentence: ")

words = sentence.split()

lword = words[0]
length = len(lword)

for word in words:
    if len(word) > length:
        lword = word
        length = len(lword)
        
print('The longest word is:', lword)

'''
>>> 
==== RESTART: C:\Users\Charlize\Documents\Python\p38_Find_Longest_Word.py ====
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The longest word is: quick
>>>
'''
