# Program Name: Midterm_Longer_Program_revised.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 10/28/18 - 10/28/18
# Description: Write a program that lets the user enter 4 sides and 4 angles.
# The program checks if the type of quadrilateral is either: Rhombus, Square, or
# Rectangle.

repeat = 1

while repeat == 1:
    print("=== Please enter Sides ===")

    sides = []
    
    for sidecnt in range(1, 5, 1):
        side = 0
        while side <= 0:
            side = float(input("Please enter side %i: " %sidecnt))
            if side <= 0:
                print("Value must be greater than zero! ")
        sides.append(side)

    print("=== Please enter Angles ===")

    angles = []

    for anglecnt in range(1, 5, 1):        
        angle = 0
        while angle <= 0:
            angle = float(input("Please enter angle %i: " %anglecnt))
            if angle <= 0:
                print("Value must be greater than zero! ")
        angles.append(angle)

    print("=======================")

    if sides[0] == sides[1] and \
       sides[1] == sides[2] and \
       sides[2] == sides[3] and \
       angles[0] == angles[1] and \
       angles[1] == angles[2] and \
       angles[2] == angles[3]:
        print("The shape is a SQUARE!")
        
    elif sides[0] == sides[1] and \
       sides[1] == sides[2] and \
       sides[2] == sides[3] and \
       angles[0] == angles[2] and \
       angles[1] == angles[3]:
        print("The shape is a RHOMBUS!")

    elif sides[0] == sides[2] and \
       sides[1] == sides[3] and \
       angles[0] == angles[1] and \
       angles[1] == angles[2] and \
       angles[2] == angles[3]:
        print("The shape is a RECTANGLE!")

    repeat = int(input("Would you like to repeat? (1-Yes, 2-No):"))


'''
>>>
 RESTART: C:/Users/Charlize/Documents/Python/Midterm_Longer_Program_revised.py 
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
