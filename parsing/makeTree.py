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

def addResult(tree, result):
	#print("we here")

	if(result == "1/2-1/2"):
		tree.draws += 1
	if(result == "1-0"):
		tree.whiteW += 1
	if(result == "0-1"):
		tree.blackW += 1

def addGame(moveSet, tree, result):
	move = moveSet.pop(0)

	if(containsMove(tree, move)):
		#add result
		addResult(tree, result)

		if(len(moveSet) > 0):
			addGame(moveSet, getMove(tree, move), result)
	#unique set of moves
	else:
		tree.moves.append(moveTree())
		tree.moves[len(tree.moves) - 1].name = move
		#add result
		addResult(tree.moves[len(tree.moves) - 1], result)

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
print("num lines is ", num_lines)

#CHANGE
for x in range(10):
	readGame(moveSet)

white = 0
black = 0
draw = 0

white2 = 0
black2 = 0
draw2 = 0
origin.printValues()

for x in origin.moves:
	white += x.whiteW
	black += x.blackW
	draw += x.draws
	for y in x.moves:
		white2 += y.whiteW
		black2 += y.blackW
		draw2 += y.draws

print(white)
print(black)
print(draw)

print(white2)
print(black2)
print(draw2)