# story layout: go to stables or king to find clue to go to a place that will lead you to the sorceress' lair. Old wise guy "right is the way of evil" and then ask which path they should go on

#timer on the game????
import time
startTime = None
def start():
	global startTime
	startTime = time.time()
	print("Welcome to Text Adventures! In this game, you will be taken through a series of steps in order to restore order in the kingdom. Be careful what you choose, as some paths may take longer than others. For picking the wrong path, you may be penalized with time deduction. Be thorough, but not too thorough in your search. Remember, the clock is ticking! All choices you make in this quest will require an answer of 1 or 2, so make sure to remember to use these answer choices only.")

	result = input("\n\n\nYou are here to save the prince!\n\nHe has been kidnapped by the evil sorceress that curses our kingdom. First, you must look for clues as to where the sorceress could have taken him.\n\nYou can either: \n1) Visit the throne room or \n2) Visit the stables.\n\n>> ")

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
		timedout = input("\n\nOh no! You took too much time to save the prince, and now the sorceress has whisked him away to a world where he could never be found. You've failed your quest! The kingdom will now fall into eternal mourning, the curse set upon the kingdom by the sorceress. Would you like to try to save the prince again? ")
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
	king = input("\n\nThe king is in much distress, but they say he was the last one to see his son before the abduction.\n\nDo you \n1) ask him for clues or \n2) let him grieve in peace and head to the stables?\n\n>> ")

	if checkInput(king, '1', '2') == '1':
		kingClue()
	elif checkInput(king, '1', '2') == '2':
		peaceGrieve()

def stables():
	checkTime()
	stableBoy = input("\n\nThe stable boy is looking for the horse, Misty, that the prince was riding when he was abducted. Misty was last seen at the garden with the prince, who was tending to his favorite sunflower patch. The stable boy seems very sad, as Misty was his favorite horse to take care of. Misty always 'knew the right way to go about things.' Would you like to 1) go to the garden or 2) help the stable boy find Misty? \n\n>> ")
	if checkInput(stableBoy, '1', '2') == '1':
		garden()
	elif checkInput(stableBoy, '1', '2') = '2':
		findMisty()

def findMisty():
	global startTime
	checkTime()
	startTime += 30
	print("\n\nYou spend an hour looking for Misty, while time to save the prince ticks by. Then, a thought occurs to you. The prince could have been abducted along with Misty! After all, the sorceress could have somehow led them through a spell to her lair. You decide that you must go back to the garden and follow the stable boy's original clue.\n\n>>")
	garden()

def kingClue():
	checkTime()
	clue = input("\n\nMy boy, oh my boy! What will we ever do? He was my pride and joy, that boy. He was so fond of that garden of ours, that he spent every waking minute in it tending to the sunflowers. Not to mention the second thing he was most fond of - his favorite horse, Misty! He always brought her to that garden with him. That wretched sorceress dragged him off because she was jealous of my happiness. Just remember one thing! The sorceress once told me (back when she was a normal person) that 'Right is the way of evil.'\n\nNow that you have gained this clue, do you wish to 1) go straight to the garden or 2) talk to the stable boy to gain more clues?\n\n>> ")
	if checkInput(clue, '1', '2') == '1':
		garden()
	if checkInput(clue, '1', '2') == '2':
		stables()

def peaceGrieve():
	checkTime()
	queen = input("\n\nNow that you left the king to grieve in peace, you encounter the queen walking back from her morning walk around the gardens. She tells you that her husband would answer any questions asked to him in this period of grieving because he is determined to find his son and bring him back. Do you 1) go back to the throne room to talk to the king or 2) head to the stables?\n\n>> ")
	if checkInput(queen, '1', '2') == '1':
		throneRoom()
	elif checkInput(queen, '1', '2') == '2':
		stables()

def garden():
	checkTime()
	garden = input("\n\nNow that you have found the sunflowers, you notice something interesting about the sunflowers closest to the forest. It looks like they were trampled by something somehow, maybe a horse. It looks as though the prince went this way! There are two paths into the forest. Do you go to the\n1) left or the\n2) right? ")
	if checkInput(garden, '1', '2') == '1':
		leftPath()
	elif checkInput(garden, '1', '2') == '2':
		rightPath()

def leftPath():
	checkTime()
	leftChoice = input("\n\nThe path ahead is windy and filled with chilly winds. Knowing that the sorceress has a knack for picking scary places to set up her lair, you are reassured by the state of this path leading you to your destiny. Do you want to\n1) continue down the left path or\n2) turn back to choose between paths again? ")
	if checkInput(leftChoice, '1', '2') == '1':
		continueLeft()
	elif checkInput(leftChoice, '1', '2') == '2':
		garden()

def continueLeft():
	global startTime
	checkTime()
	startTime += 30
	print("\n\nYou walked for quite a while and have now come to a dead end in the road. Looks like you didn't heed the advice you were given very well!")
	garden()

def rightPath():
	checkTime()
	rightChoice = input("\n\nThe path ahead is calm and clear, as hot as a summer day. It definitely doesn't give off the vibe of a path leading to a scary secret lair. But then again, looks are often deceiving. Do you want to \n1) continue down the right path or\n2) turn back and choose between paths again? ")
	if checkInput(rightChoice, '1', '2') == '1':
		continueRight()
	elif checkInput(rightChoice, '1', '2') == '2':
		garden()

start()