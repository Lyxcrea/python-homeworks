def stars(numStars):
    for i in range(0,numStars,1): # a loop to show numStars
        print("*", end=' ')
    print()

def message():
    # A couple of lines with a message
    print("   Welcome to CSIS9!")
    print("Programming can be fun!")

def main(): # a function that will start the program

    stars(10)    
    message()
    stars(10)

main()
