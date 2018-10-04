# This is the link on string splitting:
# https://www.geeksforgeeks.org/python-string-split/


# I spent an hour and really couldn't figure out how to count the spaces next to the bomb and show the number. This is my try.
# the grid starts with (0,0) at the top left corner, and with the first row being 0 value for (x,y) (sort of like the axis if it was a coordinate grid)

import sys
import random as r
flagCount = 0
while True:
	try:
		w = int(sys.argv[1]) + 2
		h = int(sys.argv[2]) + 2
		b = int(sys.argv[3])
		break
	except ValueError:
		print("Sorry, that is not an integer! Try again.")
field = [[0]*w for x in range(h)]
# debug/check if it works
#for x in range(len(field)):
	#print(*field[x])

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
# print at the end with 0s turning into the right number
# is there a way to "hide" a board or solution?
# this is my "hidden solution" field

for y in range(1,h-1):
	for x in range(1,w-1):
		print(field[y][x],end=" ")
	print("")

# use "X" or 0?
def printUserField():
	userField = [["X"]*w for x in range(h)]
	for y in range(1,h-1):
		for x in range(1,w-1):
			print(userField[y][x],end=" ")
		print("")

def choose():
	space = input("Choose a space to either clear or flag. Provide the x and y coordinates, and type 'f' for flag and 'c' for clear. Enter your answer in the following format: x, y, [f or c]") # can command line arguments work outside first python file calling
	# if flag, else (else if clear)
	userChoice = space.split(', ')
	y = userChoice[1]
	x = userChoice[0]
	if userChoice[2] == "f":
		userField[y][x] == "f"
		flagCount += 1
		checkFlags()
		printUserField()
		choose()
	else:
		# check using solution
		if field[y][x] == "*":
			gameOver()
		else:
			if field[y][x] == 0:
				# reveal contiguous spaces
				choose()
			else:
				userField[y][x] = field[y][x]
				choose()

# while loop saying while whole board is not filled, do this action, and when it is full, check to see if the flags are over bombs
# play again feature? maybe?
def gameOver():
	print("Sorry, you just unearthed a bomb!")

def checkFlags():
	if flagCount == b:
		for i in range(b):
			if userField[bombs[i][0]][bombs[i][1]] == field[bombs[i][0]][bombs[i][1]]:correctFlags += 1 
			return correctFlags
		if correctFlags == b:
			win()

# wrong this is the if statement to use for ending game checking all clear spaces and flags
		if userField[y][x] == field[y][x]:
			print("You won!")

		# check if flags are in the right spaces
def win():
	print("Yay! You won! You just swept the mines like a champ.")


printUserField()
choose()
