# Anjali Mangla
# 1/11/19
# On my honor, I have neither given nor received unauthorized aid.

# What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time? The answer is the longest walk is where you take 22 steps (or blocks), shown why after running the below simulation.
# Monte Carlo Simulations: "Monte Carlo methods (or Monte Carlo experiments) are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. Their essential idea is using randomness to solve problems that might be deterministic in principle." - Wikipedia. These simulations are very helpful in solving problems in various fields, such as physics, engineering, and computational biology.

# RANDOM WALK SIMULATION
# take random walk of n blocks
# calculate distance from home (0, 0)

import random
import matplotlib.pyplot as plt
import math

home = [0, 0] # starting position
pos = [0, 0] # current position
bus = 0
walk = 0
n = 22 # after trial and error, found that n = 22 is the closest to 50%
trials = 1000 # number of trials

# assign numbers to directions
right = 0
up = 1
left = 2
down = 3

# list will contain the calculated distance from home
distances = []

# this function returns the distance (adding up absolute values of x and y coordinates of the pos vector)
def calcDistance(pos, home):
	dist = abs(pos[0]) + abs(pos[1])
	return dist
# for loop finds a random number and, based on that, walks a step in a direction.
for j in range(trials):
	for i in range(n):
		step = random.randrange(4)
		if step == right:
			pos[0] += 1
		elif step == up:
			pos[1] += 1
		elif step == left:
			pos[0] -= 1
		elif step == down:
			pos[1] -= 1
	# append distance to distances list
	distances.append(calcDistance(pos, home))
	# pos must reset to 0, 0 before each subsequent trial
	pos = [0, 0]

# calculate how many times you will be walking
for dist in distances:
	if dist <= 4:
		walk += 1
	else:
		bus += 1
# print statements show the percentage of walking and how many walks and bus rides
print(walk, "walks and", bus, "bus rides.")
print("You are walking", 100*(walk/len(distances)),"percent of the time.")

# DARTS SIMULATION

# square is 2x2, which means our x and y graph has corners (-2, 2), (-2, -2), (2, 2), and (2, -2). For the simulation, I will randomly generate x and y coordinates for the dart within ranges from -2 to 2 for x and y. Then, I will check to see whether that position is within the radius of the circle (which is 1) or not.

pos = [0, 0]
trials = 100000
circle = 0 # keeps count of how many lands in the circle
# are the random values floats or integers? use randrange or uniform?
for i in range(trials):
	pos[0] = random.uniform(-1, 1)
	pos[1] = random.uniform(-1, 1)
	dart_dist = math.sqrt((pos[0])**2 + (pos[1])**2)
	if dart_dist <= 1:
		circle += 1

print((circle * 4) / trials)

# always gets around 3.14 with random.uniform, which approximates pi



