"""
main program
"""
import helper as h
import instructions
import classVault as c
from numberGuessingGame import runGame

print("starting")

settings = c.Settings()

def Print_Menu_Main():
    h.clearScreen()
    print(20 * "=", "Welcome to The Number Game!", 20 * "=")
    print(8 * "=","Select from the following:",8 * "=")
    print("1. New Game")
    print("2. Instructions")
    print("3. Settings")
    print("4. Clear Screen")
    print("5. Quit")
    print(70 * "=")

loopMain = True #start loop

def EndLoop():
    loopMain = False

while loopMain: #while loop will keep runnning until loop = False
    currentMenuRange = 5
    Print_Menu_Main() #Display Main Menu
    choice = input("Enter your choice [1-5]: ")

    if choice == "1":
        #print("1")
        h.clearScreen()
        runGame()
    elif choice == "2":
        #h.clearScreen()
        print(instructions.rules)
        input("Press any key to return to main menu")
        #h.clearScreen()
    elif choice == "3":
        h.clearScreen()
        h.settings(settings)
        #h.clearScreen()
    elif choice == "4":
        h.clearScreen()
    elif choice == "5":
        EndLoop()
        #h.clearScreen()
        exit()
    elif choice not in range(currentMenuRange): 
        #print("not a valid choice, try again")
        h.clearScreen()