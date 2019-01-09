# Anjali Mangla
# 1/7/2018
# On my honor, I have neither given nor received unauthorized aid.

# Comments before coding: I have heard of the Monty Hall paradox before, and I always forget the math of it after someone explains it to me, but I know that apparently switching is a better option because it yields a higher probability of getting the prize than not switching.

import random

# winCount tracks number of wins, loseCount tracks number of losses, and boxes is an array showing the three boxes
winCount = 0
loseCount = 0
boxes = [0,0,0]

# NOT SWITCHING
for i in range(1000):
	boxes = [0,0,0]
	# pos tracks the box holding the car keys, denoted by the 1.
	pos = random.randrange(0,3)
	boxes[pos] = 1
	# choice is the random box choice by the player.
	choice = random.randrange(0,3)
	# if the position of the box of the choice is the same as the position of the car, you win.
	if choice == pos:
		winCount += 1
	else:
		loseCount += 1
# print wins and losses.
print(winCount, "wins by not switching the chosen box.")
print(loseCount, "losses by not switching the chosen box.")
# counts of wins and losses are reset before the switching trial.
winCount = 0
loseCount = 0

# SWITCHING
for i in range(1000):
	boxes = [0,0,0]
	# set the car behind a random door and set choice on a random box
	pos = random.randrange(0,3)
	boxes[pos] = 1
	choice = random.randrange(0,3)
	# loop through the boxes list and reveal the first box which is a 0 (symbol for a penny) that isn't at the same position as the user's choice.
	for j in range(len(boxes)):
		if boxes[j] == 0 and j != choice:
			# even though the revealed variable isn't used, it still helps with visualization
			revealed = boxes[j]
			break
		else:
			pass
	# loop through the boxes list once again in order to switch the choice to make choice at the k position where it was not already there before and isn't the j box which was revealed
	for k in range(len(boxes)):
		if choice != k and j != k:
			choice = k
			break
		else:
			pass
	# same as in switching, check if choice is at the same position as the car and print wins and losses.
	if choice == pos:
		winCount += 1
	else:
		loseCount += 1
print(winCount, "wins by switching the chosen box.")
print(loseCount, "losses by switching the chosen box.")

# Comments explaining this paradox: The math of the Monty Hall Simulation may seem complicated and a weird phenomenon since at first most people think you have an equal chance between switching and staying, but you can explain it very easily. Since you have three boxes with 2 0s and one 1 which is the car box, think about it this way: in the case that you remain on the first box you pick, the probability that box is a 1 is a 1/3, since there is one win outcome possible out of 3 total outcomes. However, in the switching scenario, you are banking on the fact that you chose a 0 in the first place, which is 2 outcomes out of 3 outcomes, giving a probability of 2/3, since one 0 is revealed and switching would give you the car. Thus, the simulation returns with around 300-400 (around 333/1000) wins with switching which is roughly a 1/3 ratio with the sample size of trials, and 600-700 (around 667/1000) wins with not switching which is roughly a 2/3 ratio with the sample size of trials.
