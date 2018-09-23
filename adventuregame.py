# story layout: go to stables or king to find clue to go to a place that will lead you to the sorceress' lair. Old wise guy "right is the way of evil" and then ask which path they should go on

#timer on the game????
import time
startTime = None
def start():
	global startTime
	startTime = time.time()
	print("Welcome to Text Adventures! In this game, you will be taken through a series of steps in order to restore order in the kingdom. Be careful what you choose, as some paths may take longer than others. Be thorough, but not too thorough in your search. Remember, all choices you make in this quest will require an answer of 1 or 2, so make sure to remember to use these answer choices only. ")

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

	if checkInput(result, '1', '2') == '1':
		throneRoom()
	elif checkInput(result, '1', '2') == '2':
		stables()

def checkTime():
	if (time.time() < startTime + 300):
		pass
	else:
		timedout = input("Oh no! You took too much time to save the prince, and now the sorceress has whisked him away to a world where he could never be found. You've failed your quest! The kingdom will now fall into eternal mourning, the curse set upon the kingdom by the sorceress. Would you like to try to save the prince again? ")
		if checkInput(timedout, 'N', 'Y') == 'N':
			print("Oh well. The kingdom will remain desolate until the next hero comes along. Thanks for trying!")
		elif checkInput(timedout, 'N', 'Y') == 'Y':
			start()

def checkInput(choice, a, b):
	while choice != a or choice != b:
		print("I don't know what " + choice + " means. Try typing a "+a+" or a "+b+". ")
	return choice

def throneRoom():
	checkTime()
	king = input("\n\nThe king is in much distress, but they say he was the last one to see his son before the abduction.\n\nDo you \n1) ask him for clues or \n2) let him grieve in peace?\n\n>>")

	if checkInput(king, '1', '2') == '1':
		pass
		kingClue() # have the clue lead them to somewhere that would lead them to where the stables would lead them
	elif checkInput(king, '1', '2') == '2':
		pass
		peaceGrieve() # have them go now to the stables

def stables():
	checkTime()
	stableBoy = input("\n\nThe stable boy is looking for the horse, Misty, that the prince was riding when he was abducted. However, he forgot if Misty likes 1) carrots or 2) peanuts. What will you use to lure Misty? ")
	if checkInput(stableBoy, '1', '2') == '1':
		pass
	elif checkInput(stableBoy, '1', '2') = '2':
		pass

def kingClue():
	checkTime()
	clue = input("\n\nMy boy, oh my boy! What will we ever do? He was my pride and joy, that boy. He was so found of that garden of ours, that he spent every waking minute in it tending to the sunflowers. That wretched wench dragged him off because she was jealous of my happiness.\n\nNow that you have gained this clue, do you wish to 1) go straight to the garden or 2) talk to the stable boy to gain more clues?\n\n>>")
	if checkInput(clue, '1', '2') == '1':
		pass
	if checkInput(clue, '1', '2') == '2':
		stables()

def peaceGrieve():
	pass

start()