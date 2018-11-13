# Program Name: p46_File_Write_and_Read.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/3/18 - 11/3/18
# Description: Write a program to do the following:
# 1) User enters a file name (such as "myMovies.txt").
# 2) User enters the titles of 4 of their favorite movies (use a loop!).
# 3) Program Writes the 4 titles to a file, one per line, then closes the file
# (use a loop!).
# 4) Program Reads the 4 titles from "myMovies.txt" stores them in a list and
# shows the list.
# 5) The program writes the titles in reverse order into a file
# "reverseOrder.txt"
# 6) Submit the 3 files (your "p43.py" program and the two files "myMoveis.txt" and "reverseOrder.txt")


filename = input("Please enter a file name: ")

myFile = open(filename, 'w')

titles = []

for titlecnt in range (1, 5, 1):
    title = input("Please enter movie title #%i: " %titlecnt)
    titles.append(title)
print()

print("Writing the 4 movie titles to file '%s'" %filename)
for title in titles:
    myFile.write(title + '\n')
        
myFile.close()
print()

print("Reading the 4 movie titles from file into a list: ", titles)
print()

myFile = open("reverseOrder.txt", 'w')

print("Writing 4 movie titles in reverse to 'reverseOrder.txt'")
for i in range (4, 0, -1):
    myFile.write(titles[i - 1] + '\n')
            
myFile.close()
print()

print("Content of %s:" %filename)
myFile = open(filename, 'r')
titles = myFile.read().splitlines()
for title in titles:
    print(title)
myFile.close()
print()

print("Content of %s:" %'reverseOrder.txt')
myFile = open("reverseOrder.txt", 'r')
titles = myFile.read().splitlines()
for title in titles:
    print(title)
myFile.close()
print()


'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p46_File_Write_and_Read.py ===
Please enter a file name: 
=== RESTART: C:\Users\Charlize\Documents\Python\p46_File_Write_and_Read.py ===
Please enter a file name: myMovies.txt
Please enter movie title #1: movie1
Please enter movie title #2: movie2
Please enter movie title #3: movie3
Please enter movie title #4: movie4

Writing the 4 movie titles to file 'myMovies.txt'

Reading the 4 movie titles from file into a list:  ['movie1', 'movie2', 'movie3', 'movie4']

Writing 4 movie titles in reverse to 'reverseOrder.txt'

Content of myMovies.txt:
movie1
movie2
movie3
movie4

Content of reverseOrder.txt:
movie4
movie3
movie2
movie1

>>>
'''

