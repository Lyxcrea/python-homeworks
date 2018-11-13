# Program Name: p22_Dice.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/28/18 - 9/29/18
# Description: Write a Dice Game program that generates two random dice values
# between 1 and 6 for you, and 2 for the computer.

print("Beat the computer!")

from random import randint

while True:
    d1 = randint(1,6)
    d2 = randint(1,6)

    keep1 = input("You rolled %i and %i (total of %i), keep y/n:" %(d1,d2,d1+d2))
    if keep1 == 'y':
        break

pc1 = randint(1,6)
pc2 = randint(1,6)

if pc1 + pc2 > d1+d2:
    print("The computer rolled %i and %i (total of %i)." %(pc1,pc2,pc1+pc2))
    print("You lose --computer wins!")
elif pc1+pc2 < d1 + d2:
    print("The computer rolled %i and %i (total of %i)." %(pc1,pc2,pc1+pc2))
    print("You win!")
else:
    print("The computer rolled %i and %i (total of %i)." %(pc1,pc2,pc1+pc2))
    print("Tie!")


'''
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p22_Dice.py ==========
Beat the computer!
You rolled 4 and 4 (total of 8), keep y/n:y
The computer rolled 2 and 3 (total of 5).
You win!
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p22_Dice.py ==========
Beat the computer!
You rolled 1 and 2 (total of 3), keep y/n:y
The computer rolled 3 and 5 (total of 8).
You lose --computer wins!
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p22_Dice.py ==========
Beat the computer!
You rolled 5 and 4 (total of 9), keep y/n:y
The computer rolled 5 and 4 (total of 9).
Tie!
>>>
'''
