import random

noWin = 1
guessCounter = 0
number = random.randrange(0,100,1)
def start():
	global number
	if (noWin == 0):
		number = random.randrange(0,100,1)
	else:
		pass

	guess = input("Guess the integer I'm thinking of between 0 and 100. ")

	if int(guess) > 100 and int(guess) < 0:
		print("That number's not in our range! Try again.")
	else:
		pass

	if int(guess) == number:
		win()
	elif int(guess) > number:
		lower()
	elif int(guess) < number:
		higher()


def win():
	global noWin
	global guessCounter
	guessCounter += 1
	print("Congratulations! You guessed the number I was thinking of.")
	print("It took you " + str(guessCounter) + " tries.")
	guessCounter = 0
	playAgain = input("Would you like to play again? Type Y or N. ")
	if playAgain == "Y":
		noWin = 0
		start()
	elif playAgain == "N":
		pass
	else:
		print("I couldn't understand you because you didn't say Y or N, so I'm going to take that as a no.")
		pass

def lower():
	global noWin
	global guessCounter
	print("The number is lower than what you guessed. Guess again!")
	guessCounter += 1
	noWin = 1
	start()

def higher():
	global noWin
	global guessCounter
	print("The number is higher than what you guessed. Guess again!")
	guessCounter += 1
	noWin = 1
	start()

start()