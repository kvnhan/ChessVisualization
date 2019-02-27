import ast
import glob

class moveTree:
    def __init__(self):
        self.name = ""
        self.whiteW = 0
        self.blackW = 0
        self.draws = 0
        self.numInstances = 0
        self.moves = []

    def printValues(self):
        print("Name = " + self.name)
        print("White wins = ", self.whiteW)
        print("Black Wins= ", self.blackW)
        print("Draws = ", self.draws)
        print("Num Instances = ", self.numInstances)
        print("Moves size = ", len(self.moves))

    def getStatistics(self):
        r = {}
        print("TODO") #TODO
        return r

def containsMove(moveTree, move):
    for mv in moveTree.moves:
        if(mv.name == move):
            return True
    return False 

def getMove(moveTree, move):
    for mv in moveTree.moves:
        if(mv.name == move):
            return mv

def addResult(tree, result):
    #print("we here")

        if(result == "1/2-1/2"):
            tree.draws += 1
        elif(result == "1-0"):
            tree.whiteW += 1
        elif(result == "0-1"):
            tree.blackW += 1
        else:
            return -1

        tree.numInstances += 1
        return 0

def addGame(moveSet, tree, result):
    move = moveSet.pop(0)

    if(containsMove(tree, move)):
        #add result
            if(addResult(tree, result) == -1):
                return

            if(len(moveSet) > 0):
                addGame(moveSet, getMove(tree, move), result)
        #unique set of moves
    else:
        tree.moves.append(moveTree())
        tree.moves[len(tree.moves) - 1].name = move

        #add result
        if(addResult(tree, result) == -1):
            return

        if(len(moveSet) > 0):
            addGame(moveSet, getMove(tree, move), result)

def readGame(moveSet):
    game = moveSet.readline()
    game = ast.literal_eval(game)

    result = game.get('r')
    moves = game.get('g')
    result = result.split('"')[1]

    moves = moves.split('.')
    moves.pop(0)

    mvList = []
    for mv in moves:
        mv = mv.split()
        if(len(mv) > 2):
            mv.pop(2)
        mvList.extend(mv)


    if(len(mvList) > 0):
        addGame(mvList, origin, result)

def formatReturn(move):
    move.printValues()
    return "Looks like a valid set";
    

origin = moveTree()
origin.name = "origin"
'''
moveSet = open("carlsen.pgn", "r")

num_lines = sum(1 for line in open('carlsen.pgn'))

#CHANGE
for x in range(num_lines):
        readGame(moveSet)
'''
for filename in glob.glob('parsing/data/*.pgn'):
    print(filename)
    with open(filename) as f:
        numlines = sum(1 for line in open(filename))
        print("numlines:" + str(numlines))
        for x in range(numlines):
            readGame(f)

origin.printValues()
