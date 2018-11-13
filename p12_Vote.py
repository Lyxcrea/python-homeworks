# Program Name: p12_Vote.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/8/18 - 9/8/18
# Description: Write a progam to determine if the user can vote. The program
# will ask the user a series of questions - age, citizienship and registration.
# The user will receive a message as to whether or not s/he may vote -- yes,no
# (with a reason- too young, not a citizen, hasn't registered to vote.)

age = int(input("How old are you?: "))
citizen = input("Are you a U.S. citizen? (yes/no): ")
registration = input("Have you registered to vote? (yes/no): ")

if age >= 18 and citizen == 'yes' and registration == 'yes':
    print("Congratulations, you can vote!")
else:
    print("Sorry, you cannot vote.")

    if age < 18:
          print("- You must be over 18 to vote.")
    if citizen != 'yes':
          print("- You must be citizen to vote.")
    if registration != 'yes':
          print("- You must be registered to vote.")


'''
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p12_Vote.py ==========
How old are you?: 20
Are you a U.S. citizen? (yes/no): yes
Have you registered to vote? (yes/no): no
Sorry, you cannot vote.
- You must be registered to vote.
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p12_Vote.py ==========
How old are you?: 20
Are you a U.S. citizen? (yes/no): no
Have you registered to vote? (yes/no): no
Sorry, you cannot vote.
- You must be citizen to vote.
- You must be registered to vote.
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p12_Vote.py ==========
How old are you?: 17
Are you a U.S. citizen? (yes/no): no
Have you registered to vote? (yes/no): no
Sorry, you cannot vote.
- You must be over 18 to vote.
- You must be citizen to vote.
- You must be registered to vote.
>>> 
========== RESTART: C:\Users\Charlize\Documents\Python\p12_Vote.py ==========
How old are you?: 20
Are you a U.S. citizen? (yes/no): yes
Have you registered to vote? (yes/no): yes
Congratulations, you can vote!
>>>
'''
