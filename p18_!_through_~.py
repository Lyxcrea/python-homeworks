# Program Name: p18_!_through_~.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/21/18 - 9/22/18
# Description: Write a program that displays the characters in the ASCII
# character table from ! to ~.

temp = 0
count = 10
for asciiValue in range (33,127,1):
    temp += 1
    print(chr(asciiValue), end = ' ')
    asciiValue = asciiValue + 1
    if temp == count:
        print()
        temp = 0


'''
>>> 
======= RESTART: C:\Users\Charlize\Documents\Python\p18_!_through_~.py =======
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
>>>
'''
