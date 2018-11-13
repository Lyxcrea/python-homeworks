# Program Name: p11_rock,paper,scissors.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/2/18 - 9/3/18
# Description: Write a program to simulate a rock-paper-scissors game.

import random

p1 = int(input("Enter (1)Rock, (2)Paper, (3)Scissors "))
p2 = random. randint(1,3)
print("Player 1: %s" %(p1))
print("Player 2: %s" %(p2))

rock = 1
paper = 2
scissors = 3

if p1 == 1 and p2 == 3:
    print("Player 1 wins, rock breaks scissors!")
elif p1 == 2 and p2 == 1:
    print("Player 1 wins, paper covers rock!")
elif p1 == 3 and p2 == 2:
    print("Player 1 wins, scissors cuts paper!")

elif p2 == 1 and p1 == 3:
    print("Player 2 wins, rock breaks scissors!")
elif p2 == 2 and p1 == 1:
    print("Player 2 wins, paper covers rock!")
elif p2 == 3 and p1 == 2:
    print("Player 2 wins, scissors cuts paper!")

elif p1 == 1 and p2 == 1:
    print("Player 1 and Player 2 tie!")
elif p1 == 2 and p2 == 2:
    print("Player 1 and Player 2 tie!")
elif p1 == 3 and p2 == 3:
    print("Player 1 and Player 2 tie!")


'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p11_rock,paper,scissors.py ===
Enter (1)Rock, (2)Paper, (3)Scissors 1
Player 1: 1
Player 2: 3
Player 1 wins, rock breaks scissors!
>>>
=== RESTART: C:\Users\Charlize\Documents\Python\p11_rock,paper,scissors.py ===
Enter (1)Rock, (2)Paper, (3)Scissors 3
Player 1: 3
Player 2: 2
Player 1 wins, scissors cuts paper!
>>>
=== RESTART: C:\Users\Charlize\Documents\Python\p11_rock,paper,scissors.py ===
Enter (1)Rock, (2)Paper, (3)Scissors 2
Player 1: 2
Player 2: 1
Player 1 wins, paper covers rock!
>>>
=== RESTART: C:\Users\Charlize\Documents\Python\p11_rock,paper,scissors.py ===
Enter (1)Rock, (2)Paper, (3)Scissors 3
Player 1: 3
Player 2: 3
Player 1 and Player 2 tie!
>>>
'''
