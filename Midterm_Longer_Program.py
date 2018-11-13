# Program Name: Midterm_Longer_Program.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/27/18 - 10/27/18
# Description: Write a program that lets the user enter 4 sides and 4 angles.
# The program checks if the type of quadrilateral is either: Rhombus, Square, or
# Rectangle.

repeat = 1

while repeat == 1:
    print("=== Please enter Sides ===")
    
    side1 = 0
    while side1 <= 0:
        side1 = float(input("Please enter side 1: "))
        if side1 <= 0:
            print("Value must be greater than zero! ")

    side2 = 0
    while side2 <= 0:
        side2 = float(input("Please enter side 2: "))
        if side2 <= 0:
            print("Value must be greater than zero! ")

    side3 = 0
    while side3 <= 0:
        side3 = float(input("Please enter side 3: "))
        if side3 <= 0:
            print("Value must be greater than zero! ")

    side4 = 0
    while side4 <= 0:
        side4 = float(input("Please enter side 4: "))
        if side4 <= 0:
            print("Value must be greater than zero! ")

    print("=== Please enter Angles ===")
    
    angle1 = 0
    while angle1 <= 0:
        angle1 = float(input("Please enter angle 1: "))
        if angle1 <= 0:
            print("Value must be greater than zero! ")

    angle2 = 0
    while angle2 <= 0:
        angle2 = float(input("Please enter angle 2: "))
        if angle2 <= 0:
            print("Value must be greater than zero! ")

    angle3 = 0
    while angle3 <= 0:
        angle3 = float(input("Please enter angle 3: "))
        if angle3 <= 0:
            print("Value must be greater than zero! ")

    angle4 = 0
    while angle4 <= 0:
        angle4 = float(input("Please enter angle 4: "))
        if angle4 <= 0:
            print("Value must be greater than zero! ")

    print("=======================")

    if side1 == side2 and side2 == side3 and side3 == side4 and \
       angle1 == angle2 and angle2 == angle3 and angle3 == angle4:
        print("The shape is a SQUARE!")
        
    elif side1 == side2 and side2 == side3 and side3 == side4 and \
       angle1 == angle3 and angle2 == angle4:
        print("The shape is a RHOMBUS!")

    elif side1 == side3 and side2 == side4 and \
       angle1 == angle2 and angle2 == angle3 and angle3 == angle4:
        print("The shape is a RECTANGLE!")

    repeat = int(input("Would you like to repeat? (1-Yes, 2-No):"))


'''
>>>
=== RESTART: C:/Users/Charlize/Documents/Python/Midterm_Longer_Program.py ===
=== Please enter Sides ===
Please enter side 1: -1
Value must be greater than zero! 
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: -1
Value must be greater than zero! 
Please enter side 3: 1
Please enter side 4: 1
=== Please enter Angles ===
Please enter angle 1: -1
Value must be greater than zero! 
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: -1
Value must be greater than zero! 
Please enter angle 3: 90
Please enter angle 4: 90
=======================
The shape is a SQUARE!
Would you like to repeat? (1-Yes, 2-No):1
=== Please enter Sides ===
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1
=== Please enter Angles ===
Please enter angle 1: 120
Please enter angle 2: 60
Please enter angle 3: 120
Please enter angle 4: 60
=======================
The shape is a RHOMBUS!
Would you like to repeat? (1-Yes, 2-No):1
=== Please enter Sides ===
Please enter side 1: 10
Please enter side 2: 20
Please enter side 3: 10
Please enter side 4: 20
=== Please enter Angles ===
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: 90
Please enter angle 4: 90
=======================
The shape is a RECTANGLE!
Would you like to repeat? (1-Yes, 2-No):2
>>>
'''

    
