# I spent an hour and really couldn't figure out how to count the spaces next to the bomb and show the number. This is my try.
# the grid starts with (0,0) at the top left corner, and with the first row being 0 value for (x,y) (sort of like the axis if it was a coordinate grid)

import sys
import random as r

while True:
	try:
		w = int(sys.argv[1])
		h = int(sys.argv[2])
		b = int(sys.argv[3])
		break
	except ValueError:
		print("Sorry, that is not an integer! Try again.")
field = [[0]*w for x in range(h)]

for x in range(len(field)):
	print(*field[x])

# I found that randint was better than randrange because it includes the last number in it: https://stackoverflow.com/questions/3540431/difference-between-random-randint-vs-randrange

for number in range(b):
	x = r.randrange(w)
	y = r.randrange(h)
	print(x)
	print(y)
	field[y][x] = "*"

for x in range(len(field)):
	print(*field[x])

def checkAround():
	global current
	current = field[y][x]
	if x + 1 <= w:
		if field[y][x+1] == "*":
			# one position to the right
			current += 1
	elif x - 1 >= 0:
		if field[y][x-1] == "*":
			# one position to the left
			current += 1
	elif y + 1 <= y:
		if field[y+1][x] == "*":
			# one position above
			current += 1
	elif y - 1 >= 0:
		if field[y-1][x] == "*":
			# one position below
			current += 1
	elif x + 1 <= w and y + 1 <= h:
		if field[y+1][x+1] == "*":
			current += 1
	elif x + 1 <= w and y - 1 >= 0:
		if field[y-1][x+1] == "*":
			current += 1
	elif x - 1 <= 0 and y + 1 <= h:
		if field[y+1][x-1] == "*":
			current += 1
	elif x - 1 <= 0 and y - 1 >= 0:
		if field[y-1][x-1] == "*":
			current += 1

for a in range(y*x):
	current = field[y][x]
	if current == "*":
		checkAround()

for x in range(len(field)):
	print(*field[x])
