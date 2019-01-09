import random
flips = 0
trial = 10*flips
heads = 0
counter = 0

numbers = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
	for j in range(10):
		for k in range(10):
			flip = random.randint(0,1)
			if flip == 0:
				heads += 1
		#print("number of heads:", heads)
		numbers[heads] += 1
		heads = 0

print(numbers)






