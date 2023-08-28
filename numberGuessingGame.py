"""
2 player game
both players are given the same target number
both players are give n number of basic math operators (+, -, /, x)
both players are given the same number for each "turn"
player chooses the math operator they want to apply
games ends when n operators have been used
player closest to target number wins 
"""
import helper as h
import classVault as c

settings = c.Settings

def runGame():
    class Person:

        #Type annotations
        __playerNumber: int
        __name: str
        __currentNumber: float
        __oCountAdd: int
        __oCountSub: int
        __oCountMult: int
        __oCountDiv: int
        __result: float
        instances: set
        isDed: bool

        # Initializing variables
        no_of_players = 0
        instances = set()

        def __init__(self):#, name="test name"):
            #self.__name=name
            Person.no_of_players += 1
            Person.instances.add(self)
            Person.isDed = False

        #@property
        # def result(self):
        #     return self.__result
        
        # def showClosestPlayer(self):
        #     closestPlayer =  self.__result[0]
        #     for i in self.__result[1:]:
        #         if i.__result < closestPlayer.__result:
        #             closestPlayer = i
        #     return closestPlayer

        #def newPlayer(self, tmpName):
        #    Person.name = tmpName

        #This is where mian game code will go
        # Create another loop.
        #Loops checks turns left, if more than 0 then reloop
        #This should get around the issue we had with removing players from a game
        #create settings menu class which has defaults, or can be adjusted from a settings menu in main.py.
        #Set this before or after class declaration?


    #start
    playerCount = int(input("how many players? "))
    playerArray = [Person() for i in range(playerCount)]
    playerNum = 0
    for playerNum, player in enumerate(playerArray, start=1):
        player.__name = str(input("Player "+str(playerNum)+" enter your name: "))
        h.clearScreen()        


    print("num players: ",Person.no_of_players)
    #print("instances: ",Person.instances)
    #instances:  {<__main__.Person object at 0x00000227163A7E80>, <__main__.Person object at 0x00000227163A4640>}

    """
    This is an example of accessing list of class we have instantiated (is that the right word?)
    for i in playerArray:
        print(i.__name)
    """

    #setup initial start conditions:
    #start and target #'s
    targetNo = h.randomIntGenerator()
    startNo = h.randomIntGenerator()

    mult='*'
    div='/'
    add='+'
    sub='-'

    #seed operations for players
    startingOperands = h.generateOperands()
    multCount = startingOperands.count(mult)
    divCount = startingOperands.count(div)
    addCount = startingOperands.count(add)
    subCount = startingOperands.count(sub)
    for player in playerArray:
        player.__currentNumber = startNo
        player.__oCountMult = multCount
        player.__oCountDiv = divCount
        player.__oCountAdd = addCount
        player.__oCountSub = subCount

    #get number of rounds
    turnsLeft = settings.noRounds

    h.startGame(targetNo, startNo, multCount, divCount, addCount, subCount)

    playersLeft = len(playerArray)

    
    #Begin game rounds here
    gameActive=True
    while gameActive == True:    

        if turnsLeft != 0:
            nextNumber = h.randomIntGenerator()
            for playersLeft, player in enumerate(playerArray, start=1):
                if player.isDed == False:
                    h.startNextTurn(playersLeft, turnsLeft, playerArray, nextNumber, targetNo)
                    choice = h.playerTurn(player, nextNumber, targetNo)
                    playerDed: bool
                    playerDed = h.calcChoice(choice, player, nextNumber)

                    if playerDed == True:
                        h.removePlayer(player)
                    else:
                        if choice == "":
                            print("You did not enter an operation! You came close to been ded!")
                        else:
                            h.returnChoice(choice, player)
            turnsLeft -= 1
        else:
            h.gameResults(playerArray, targetNo)
            input("Return to menu (Enter)")
            gameActive=False

    return