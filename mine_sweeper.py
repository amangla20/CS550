# I spent an hour and really couldn't figure out how to count the spaces next to the bomb and show the number. This is my try.
# the grid starts with (0,0) at the top left corner, and with the first row being 0 value for (x,y) (sort of like the axis if it was a coordinate grid)

import sys
import random as r

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

# I found that randint was better than randrange because it includes the last number in it: https://stackoverflow.com/questions/3540431/difference-between-random-randint-vs-randrange

for number in range(b):
	x = r.randrange(1,w-1)
	y = r.randrange(1,h-1)
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
for y in range(1,h-1):
	for x in range(1,w-1):
		print(field[y][x],end=" ")
	print("")

def choose():
	space = input("Choose a space to either clear or flag. Provide the x and y coordinates, and type 'f' for flag and 'c' for clear.") # can command line arguments work outside first python file calling
	if space[2] == f:
		field[space[1]][space[0]] == "f"
	else:
		if field[space[1]][space[0]] == "*":
			gameOver()
		else:
			# reveal space


