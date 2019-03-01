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
		r["name"] = self.name
		r["whiteW"] = self.whiteW
		r["blackW"] = self.blackW
		r["draw"] = self.draws
		r["numInstances"] = self.numInstances
		return r

def getNumInstances(tree):
	return tree.numInstances

def isClean(move):
	return not (move == "1-0" or move == "0-1" or move == "1-1" or move == "0" or move == "1")

def containsMove(moveTree, move):
	val = False
	for mv in moveTree.moves:
		if(mv.name == move):
			val = True
	return val

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
	if(not isClean(move)):
		return

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
	ret = {}	
	ret["move"] = move.getStatistics()	
	potMoves = []	
	for m in move.moves:	
		potMoves.append(m.getStatistics())
	ret["potMoves"] = potMoves
	print(ret)
	return ret;

origin = moveTree()
origin.name = "origin"
'''
moveSet = open("carlsen.pgn", "r")

num_lines = sum(1 for line in open('carlsen.pgn'))

#CHANGE
for x in range(num_lines):
	readGame(moveSet)
'''
for filename in glob.glob('data/*.pgn'):
	print(filename)
	with open(filename) as f:
		numlines = sum(1 for line in open(filename))
		print("numlines:" + str(numlines))
		for x in range(numlines):
			readGame(f)

#origin.printValues()

origin.getStatistics()
