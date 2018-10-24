num = 0

while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		break
	except ValueError:
		print("That's not a number. Try again.")

count = 0;

while num<1 or num>5:
	num = int(input("That's not in the right range. Pick a number between 1 and 5: "))
print("Success!")