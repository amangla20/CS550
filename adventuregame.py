# try to use a while loop checker

def start():
	result = input("\nYou are here to save the prince!\n\nHe has been kidnapped by the evil sorceress that curses our kingdom. First, you must look for clues as to where the sorceress could have taken him.\n\nYou can either: \n1) Visit the throne room or \n2) Visit the stables.\n\n>>")

	"""
	# one way to do it
	if result == '1':
		result = input("You go left or right. What do you choose?")
		if result == "left":
			pass
		elif result == "right":
			pass
		elif
"""

	if result == '1':
		throneRoom()
	elif result == '2':
		stables()
	else:
		print("I don't know what " + result + " means. Try typing a 1 or a 2.")
		start()

def throneRoom():
	king = input("\n\nThe king is in much distress, but they say he was the last one to see his son before the abduction.\n\nDo you \n1) ask him for clues or \n2) let him grieve in peace?\n\n>>")
	if king == '1':
		pass
		kingClue() # have the clue lead them to where the stables would
	elif king == '2':
		pass
		peaceGrieve() # have them go now to the stables
	else:
		print("I don't know what " + result + " means. Try typing a 1 or a 2.")
		# throneRoom()

def stables():
	stableBoy = input("\n\nThe stable boy is looking for the horse, Misty, that the prince was riding when he was abducted. However, he forgot if Misty likes 1) carrots or 2) peanuts. What will you use to lure Misty? ")
	start()

start()