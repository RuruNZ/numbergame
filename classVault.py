"""
Classes
"""

class Settings:
    lowerNumber: int
    upperNumber: int
    operationsLimit: int
    wildCards: int
    noRounds: int

    def __init__(self):
        Settings.lowerNumber = 0
        Settings.upperNumber = 1000
        Settings.operationsLimit = 10
        Settings.wildCards = 1
        Settings.noRounds = 10

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

    # Initializing variables
    no_of_players = 0
    instances = set()

    def __init__(self):#, name="test name"):
        #self.__name=name
        Person.no_of_players += 1
        Person.instances.add(self)