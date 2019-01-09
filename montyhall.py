# Anjali Mangla
# 1/7/2018
# On my honor, I have neither given nor received unauthorized aid.

# Comments before coding: I have heard of the Monty Hall paradox before, and I always forget the math of it after someone explains it to me, but I know that apparently switching is a better option because it yields a higher probability of getting the prize than not switching.

import random

winCount = 0
loseCount = 0
boxes = [0,0,0]

for i in range(1000):
	boxes = [0,0,0]
	# pos tracks the box holding the car keys, denoted by the 1.
	pos = random.randrange(0,3)
	boxes[pos] = 1
	# choice is the random box choice by the player.
	choice = random.randrange(0,3)
	if choice == pos:
		winCount += 1
	else:
		loseCount += 1
print(winCount, "wins by not switching the chosen box.")
print(loseCount, "losses by not switching the chosen box.")
winCount = 0
loseCount = 0

# 1 0 0
# choice is 1, pos is 0
# j = 0. boxes[j] = 1 so the if statement doesnt work
# j = 1. boxes[j] = 0 but j = choice so it doesn't work
# j = 2. boxes[j] = 0 and j != choice. works! j is 2 and the third box is revealed. break from the for loop
# next, choice (1) != k (0) and j (2) does not equal k, so choice now = k which is 0
for i in range(1000):
	boxes = [0,0,0]
	pos = random.randrange(0,3)
	boxes[pos] = 1
	choice = random.randrange(0,3)
	for j in range(len(boxes)):
		if boxes[j] == 0 and j != choice:
			revealed = boxes[j]
			break
		else:
			pass
	for k in range(len(boxes)):
		if choice != k and j != k:
			choice = k
			break
		else:
			pass
	if choice == pos:
		winCount += 1
	else:
		loseCount += 1
print(winCount, "wins by switching the chosen box.")
print(loseCount, "losses by switching the chosen box.")
