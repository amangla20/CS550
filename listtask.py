import random as r

#Create a list of 15 random numbers 0-100, and print it
# Ask the user for a input from 0-100
# Error checking for the user input
# Append this input to the list
# Order the list in descending order

a = []

for x in range(15):
	a.append(r.randrange(100))
print(a)

def list():
	user_input = int(input("Input a number from 0 to 100 and I'll add it to the list!"))

	if input < 0 or input > 100:
		print("Sorry, you're number is not in our range. Try again!")
		list()
	else:
		a.append(user_input)
	a.sort(reverse = True)
	print(a)

list()