# Program Name: p14_Astrology_Program.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 9/8/18 - 9/9/18
# Description: Write a program that asks the user for day and month of a
# birthday. The program then tells the Zodiac signs that will be compatible with
# that birthday.

day = int(input("Please enter day of birth: "))
month = int(input("Please enter month of birth: "))

if(month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("You are Aries, Fire group, compatible with Aries, Leo, Sagittarius")
if(month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("You are Taurus, Earth group, compatible with Taurus, Virgo, Capricorn")
if(month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("You are Gemini, Air group, compatible with Gemini, Libra, Aquarius")
if(month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("You are Cancer, Water group, compatible with Cancer, Scorpio, Pisces")
if(month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("You are Leo, Fire group, compatible with Aries, Leo, Sagittarius")
if(month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("You are Virgo, Earth group, compatible with Taurus, Virgo, Capricorn")
if(month == 9 and day >= 23) or (month == 10 and day <= 23):
    print("You are Libra, Air group, compatible with Gemini, Libra, Aquarius")
if(month == 10 and day >= 24) or (month == 11 and day <= 21):
    print("You are Scorpio, Water group, compatible with Cancer, Scorpio, Pisces")
if(month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("You are Sagittarius, Fire group, compatible with Aries, Leo, Sagittarius")
if(month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("You are Capricorn, Earth group, compatible with Taurus, Virgo, Capricorn")
if(month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("You are Aquarius, Air group, compatible with Gemini, Libra, Aquarius")
if(month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("You are Pisces, Water group, compatible with Cancer, Scorpio, Pisces")
    

'''
>>> 
==== RESTART: C:\Users\Charlize\Documents\Python\p14_Astrology_Program.py ====
Please enter day of birth: 18
Please enter month of birth: 5
You are Taurus, Earth group, compatible with Taurus, Virgo, Capricorn
>>>
'''
