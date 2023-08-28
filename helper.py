"""
helper functions
"""
import os
import random
import pprint
import classVault as c

def clearScreen():
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')

def settings(settings):
    loopSettings = True #start loop

    # def EndSettings():
    #     loopSettings = False

    while loopSettings == True:
        clearScreen()
        currentMenuRange = 4
        text = """Game Settings:
    Setting [Default]
[1] Lowest number in game [0]:      {lower}
[2] Highest number in game [1000]:  {upper}
[3] Operations pool size [10]:      {operationsPool}
[4] Wild Cards per game [1]:        {wildCards}
[5] Number of rounds per game [10]: {gameRounds}
[6] Exit menu
"""
        print(text.format(upper= settings.upperNumber, lower=settings.lowerNumber , operationsPool=settings.operationsLimit, wildCards=settings.wildCards, gameRounds=settings.noRounds))
        choice = input("Enter your choice [1-5]: ")

        if choice == "1":
            try:
                c.Settings.lowerNumber = int(input("Enter new value: "))
            except:
                print("you did not enter a number")
            
        elif choice == "2":
            try:
                c.Settings.upperNumber = int(input("Enter new value: "))
            except:
                print("you did not enter a number")
            
        elif choice == "3":
            try:
                c.Settings.operationsLimit = int(input("Enter new value: "))
            except:
                print("you did not enter a number")
            
        elif choice == "4":
            try:
                c.Settings.wildCards = int(input("Enter new value: "))
            except:
                print("you did not enter a number")
                    
        elif choice == "5":
            try:
                c.Settings.noRounds = int(input("Enter new value: "))
            except:
                print("you did not enter a number")
        elif choice == "6":
            loopSettings = False

        elif choice not in range(currentMenuRange): 
            clearScreen()



def randomIntGenerator():
    n = random.randint(c.Settings.lowerNumber,c.Settings.upperNumber)
    return n

def generateOperands():
    operands=["+","-","/","*"]
    totalOperations = c.Settings.operationsLimit
    selectedOperands=()
    for i in range(totalOperations):
        newOperand = (random.choice(operands),)
        selectedOperands += newOperand
    return selectedOperands

# def assignOperands():
#     print()
#     multCount = count()
#     divCount = 0
#     addCount = 0
#     subCount = 0

def startGame(targetNo, startNo, multCount, divCount, addCount, subCount):
    startText = """The start conditions have been set
Your initial starting number is: {startNumber}
Your target number is: {targetNumber}
All players start with the following number of operands:
    -Multiply   {multCountStart}
    -Divide     {divCountStart}
    -Add        {addCountStart}
    -Subtract   {subCountStart}
    """
    clearScreen()
    print(startText.format(targetNumber=targetNo, startNumber=startNo, multCountStart=multCount, divCountStart=divCount, addCountStart=addCount, subCountStart=subCount))
    input("Press Enter when ready")
    clearScreen()
    

def startNextTurn(playersLeft, turnsLeft, playerArray, nextNumber, targetNo):
    clearScreen()
    if turnsLeft != 1:
        print("There are "+str(turnsLeft)+ " turns left")
    else:
        print("!!LAST TURN!!")
    notDedCount = 0
    for playersLeft, player in enumerate(playerArray):
        if player.isDed == False:
            notDedCount += 1
    print(str(notDedCount)+" players remain")
    for playersLeft, player in enumerate(playerArray):
        if player.isDed == False:
            print("-"+player.__name)
#    print("\nThis rounds number is: "+str(nextNumber))
#    print("The end game goal is: "+str(targetNo))

def playerTurn(player, targetNo, startNo):
    playerTurnStartText = """\nPlayer {playerName} it is your turn.
Your current number is: {playerCurNo}
You have the following operand uses left:
    -Multiply   {multCountStart}
    -Divide     {divCountStart}
    -Add        {addCountStart}
    -Subtract   {subCountStart}
Your new number for this round is: {startNumber}
The end game target number is: {targetNumber}
Choose your operation carefully, or you will removed from the game.
"""
    return input(playerTurnStartText.format(playerCurNo=player.__currentNumber, playerName=player.__name, multCountStart=player.__oCountMult, divCountStart=player.__oCountDiv, addCountStart=player.__oCountAdd, subCountStart=player.__oCountSub, targetNumber=targetNo, startNumber=startNo))

def calcChoice(choice, player, nextNumber):
        
    if choice == "*":
        if player.__oCountMult > 0:
            player.__currentNumber = round(player.__currentNumber*nextNumber,2)
            player.__oCountMult=player.__oCountMult-1
        else:
            return True
    elif choice == "/":
        if player.__oCountDiv > 0:
            player.__currentNumber = round(player.__currentNumber/nextNumber,2)
            player.__oCountDiv=player.__oCountDiv-1
        else:
            return True                    
    elif choice == "+":
        if player.__oCountAdd > 0:
            player.__currentNumber = round(player.__currentNumber+nextNumber,2)
            player.__oCountAdd=player.__oCountAdd-1
        else:
            return True
    elif choice == "-":
        if player.__oCountSub > 0:
            player.__currentNumber = round(player.__currentNumber-nextNumber,2)
            player.__oCountSub=player.__oCountSub-1
        else:
            return True
    elif choice == "":
        return False
    else:
        return True
    
def returnChoice(choice, player):
    input("Your new number is "+str(player.__currentNumber)+"\nPress Enter to end your turn")



def removePlayer(player):
    text = """Player {victim} made a mistake!
They have been removed from the game"""
    print(text.format(victim=player.__name))
    player.isDed = True
    input("Press Enter when ready")



def gameResults(playerArray, targetNo):
    clearScreen()
    resultsText1 = """The game has finished.
The target number was {target}
Player {winner} won and were {distance} from the target number.
Scoreboard will be a thing, when I make that happen.
GG
"""

    for playersLeft, player in enumerate(playerArray):
        player.__result = abs(targetNo - player.__currentNumber)
    #     print(player.__result)

    # for playersLeft, player in enumerate(playerArray):
    #     print(player.__result)

    playerResults = []
    for playersLeft, player in enumerate(playerArray):
        if player.isDed == False:
            playerResults.append({"Name": player.__name, "Result": player.__result})
    playerResults = sorted(playerResults, key=lambda x: x["Result"])

    print(resultsText1.format(target=targetNo, winner=playerResults[0]["Name"], distance=playerResults[0]["Result"]))

    for playersLeft, player in enumerate(playerArray):
        if player.isDed == True:
            playerResults.append({"Name": player.__name, "Result": int()})

    def getResult(element):
        return element['Result']
    
    print("Game results")
    pprint.pprint(sorted(playerResults, key=lambda x: x["Result"]))
    