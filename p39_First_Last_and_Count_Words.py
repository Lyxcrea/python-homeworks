# Program Name: p39_First_Last_and_Count_Words.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/20/18 - 10/20/18
# Description: Write a program that asks the user to enter a sentence. (can't
# use the built-in python function count() to do this!) Your program will: 1)
# count how many words are in the sentence 2) show the last word of the sentence
# 3) ask the user to enter their own word, and count how many times their word
# appears in the sentence.

sentence = input("Please enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    count += 1

print("There are %i words in the sentence you entered" %count)

print("The last word is '%s'" %words[count - 1])

search = input("Please enter a word to search: ")

count = 0
for word in words:
    if word.lower() == search.lower():
        count += 1
search = "'" + search + "'"
print("The word", search, "appears", count ,"times")

'''
>>> 
 RESTART: C:\Users\Charlize\Documents\Python\p39_First_Last_and_Count_Words.py 
Please enter a sentence: The fox and the dog
There are 5 words in the sentence you entered
The last word is 'dog'
Please enter a word to search: the
The word 'the' appears 2 times
>>>
'''
