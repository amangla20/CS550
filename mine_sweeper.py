# Anjali Mangla
# 10/08/2018
# This code is the code for a minesweeper game in which participants must flag all of the bombs and not uncover any bombs before they finish the game.
# This is the link on string splitting:
# https://www.geeksforgeeks.org/python-string-split/

# I spent an hour and really couldn't figure out how to count the spaces next to the bomb and show the number. This is my try.
# the grid starts with (0,0) at the top left corner, and with the first row being 0 value for (x,y) (sort of like the axis if it was a coordinate grid)
# TO ADD:
# if statement that makes amount of bombs entered less than w * h
import sys
import random as r
flags = []
# count of the spaces that have been revealed
numRevealed = 0
correctFlags = 0
bombs = []
zerosRevealed = []

while True:
	try:
		w = int(sys.argv[1]) + 2
		h = int(sys.argv[2]) + 2
		b = int(sys.argv[3])
		break
	except ValueError:
		print("Sorry, that is not an integer! Try again.")

field = [[0]*w for x in range(h)]
userField = [["X"]*w for x in range(h)]
# debug/check if it works
#for x in range(len(field)):
	#print(*field[x])
def start():
	global w
	global h
	global b
	# MAKE AN ARRAY OF THE X AND Y VALUES OF THE BOMBS
	for number in range(b):
		x = r.randrange(1,w-1)
		y = r.randrange(1,h-1)
		# array keeps track of bomb positions
		bombs.append([x,y])
		#print(x)
		#print(y)
		field[y][x] = "*"
	# debug
	#for x in range(len(field)):
		#print(*field[x])

		

	for y in range(1,h-1):
		for x in range(1,w-1):
			if field[y][x] == "*":
				if field[y][x+1] != "*":
					# one position to the right
					field[y][x+1] += 1
				if field[y][x-1] != "*":
					# one position to the left
					field[y][x-1] += 1
				if field[y+1][x] != "*":
					# one position above
					field[y+1][x] += 1
				if field[y-1][x] != "*":
					# one position below
					field[y-1][x] += 1
				if field[y+1][x+1] != "*":
					field[y+1][x+1] += 1
				if field[y-1][x+1] != "*":
					field[y-1][x+1] += 1
				if field[y+1][x-1] != "*":
					field[y+1][x-1] += 1
				if field[y-1][x-1] != "*":
					field[y-1][x-1] += 1
	printUserField()	
	choose()
	# print at the end with 0s turning into the right number
	# is there a way to "hide" a board or solution?
	# this is my "hidden solution" field
"""
	for y in range(1,h-1):
		for x in range(1,w-1):
			print(field[y][x],end=" ")
		print("")
"""
	


def choose():
	global numRevealed
	global w
	global h
	global b
	space = input("Choose a space to either clear or flag. Provide the x and y coordinates, and type 'f' for flag and 'c' for clear. Enter your answer in the following format: x, y, [f or c] ") # can command line arguments work outside first python file calling
	# if flag, else (else if clear)
	userChoice = space.split(', ')
	y = int(userChoice[1])
	x = int(userChoice[0])
	if userChoice[2] == "f":
		if userField[y][x] == "X":
			userField[y][x] = "f"
			flags.append([x,y])
			printUserField()
			checkFlags()
		else:
			print("You've already revealed that space! You can't flag it now!")
			printUserField()
			checkFlags()
	else:
		# check using solution
		if field[y][x] == "*":
			gameOver()
		else:
			if userField[y][x] == "f":
				flags.remove([x,y])
			elif field[y][x] == 0:
				# reveal contiguous spaces
				zerosRevealed.append([x,y])
				checkZeroes()
				printUserField()
				choose()
			else:
				userField[y][x] = field[y][x]
				numRevealed += 1
				# check flags even when clearing because if the last space on the board is revealed through clear, and the flags are more than the number of bombs, then checkFlags needs to be called in order to issue warning statement
				printUserField()
				checkFlags()
				

def printUserField():
	global w
	global h
	global b
	for y in range(1,h-1):
		for x in range(1,w-1):
			print(userField[y][x],end=" ")
		print("")
# while loop saying while whole board is not filled, do this action, and when it is full, check to see if the flags are over bombs
# play again feature? maybe?
def gameOver():
	print("Sorry, you just unearthed a bomb!")
# need to create a "user bombs" array
def checkFlags():
	global numRevealed
	global correctFlags
	global w
	global h
	global b
	# tell the user if they have revealed the entire board, but have too many flags, that they need to keep going
	for y in range(1,h-1):
		for x in range(1,w-1):
			if userField[y][x] != "X":
				numRevealed += 1
	if numRevealed == (w-2)*(h-2):
		print("Uh oh! Looks like you flagged some spaces that aren't bombs. Keep going!")
	# reset the number revealed variable
	numRevealed = 0
	# only useful to check if flags are in the right place if the number of flags = bombs
	if len(flags) == b:
		for i in range(b):
			if userField[bombs[i][1]][bombs[i][0]] == "f":
				correctFlags += 1
		if correctFlags == b:
			win()
		else:
			choose()
	else:
		choose()
	# needs to reupdate itself each time
	correctFlags = 0

def win():
	playAgain = input("Yay! You won! You just swept the mines like a champ.\nWould you like to play again? Answer 'Y' or 'N'")
	if playAgain == 'Y':
		field = [[0]*w for x in range(h)]
		userField = [["X"]*w for x in range(h)]
		start()

	else:
		print("Goodbye!")

def checkZeroes():
	global numRevealed
	global w
	global h
	global b
	while zerosRevealed:
		originaly = zerosRevealed[0][1]
		originalx = zerosRevealed[0][0]
		zerosRevealed.remove(zerosRevealed[0])
		for y in range(originaly-1,originaly+2):
			for x in range(originalx-1,originalx+2):				
				if field[y][x] == 0 and userField[y][x] == "X":
					if y > 0 and y < h-1 and x > 0 and x < w-1:
						zerosRevealed.append([x,y])
				userField[y][x] = field[y][x]
start()