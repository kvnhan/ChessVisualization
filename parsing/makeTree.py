import ast

class moveTree:
	def __init__(self):
		self.name = ""
		self.winPct = 0
		self.whiteW = 0
		self.blackW = 0
		self.draws = 0
		self.numInstances = 0
		self.moves = []

	def printValues(self):
		print("Name = " + self.name)
		print("Win% = ", self.winPct)
		print("White wins = ", self.whiteW)
		print("Black Wins= ", self.blackW)
		print("Draws = ", self.draws)
		print("Num Instances = ", self.numInstances)
		print("Moves size = ", len(self.moves))

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

def addGame(moveSet, tree, result):
	move = moveSet.pop(0)
	if(containsMove(tree, move)):
		if(result == "1/2-1/2"):
			tree.moves[len(tree.moves) - 1].draws += 1
		if(result == "1-0"):
			tree.moves[len(tree.moves) - 1].whiteW += 1
		if(result == "0-1"):
			tree.moves[len(tree.moves) - 1].blackW += 1
			
		if(len(moveSet) > 0):
			addGame(moveSet, getMove(tree, move), result)
	else:
		tree.moves.append(moveTree())
		tree.moves[len(tree.moves) - 1].name = move
		
		if(result == "1/2-1/2"):
			tree.moves[len(tree.moves) - 1].draws += 1
		if(result == "1-0"):
			tree.moves[len(tree.moves) - 1].whiteW += 1
		if(result == "0-1"):
			tree.moves[len(tree.moves) - 1].blackW += 1

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

origin = moveTree()
origin.name = "origin"

moveSet = open("carlsen.pgn", "r")

num_lines = sum(1 for line in open('carlsen.pgn'))

for x in range(num_lines):
	readGame(moveSet)

origin.printValues()
origin.moves[0].printValues()