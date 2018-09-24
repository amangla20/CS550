# Anjali Mangla
# 9/24/2018
# I decided to make a project about someone saving the prince for once
import time
startTime = None

def start():
	global startTime
	startTime = time.time()
	print("\n\nWelcome to Text Adventures! In this game, you will be taken through a series of steps in order to restore order in the kingdom. Be careful what you choose, as some paths may take longer than others. For picking the wrong path, you may be penalized with time deduction. Be thorough, but not too thorough in your search. Remember, the clock is ticking! You only have 5 minutes to rescue the prince. All choices you make in this quest will require an answer of 1 or 2, so make sure to remember to use these answer choices only.")

	result = input("\n\n\nYou are here to save the prince!\n\nHe has been kidnapped by the evil sorceress that curses our kingdom. First, you must look for clues as to where the sorceress could have taken him.\n\nYou can either: \n1) Visit the throne room or \n2) Visit the stables.\n\n>> ")

	if checkInput(result, '1', '2') == '1':
		throneRoom()
	elif checkInput(result, '1', '2') == '2':
		stables()

def checkTime():
	if (time.time() < startTime + 300):
		pass
	else:
		timedout = input("\n\nOh no! You took too much time to save the prince, and now the sorceress has whisked him away to a world where he could never be found. You've failed your quest! The kingdom will now fall into eternal mourning, the curse set upon the kingdom by the sorceress.\n\nWould you like to try to save the prince again?\nType 1 for yes and 2 for no.\n\n>> ")
		if checkInput(timedout, '1', '2') == '1':
			start()
		elif checkInput(timedout, '1', '2') == '2':
			print("Oh well. The kingdom will remain desolate until the next hero comes along. Thanks for trying!")

def checkInput(choice, a, b):
	
	while choice != a and choice != b:
		choice = input("I don't know what " + choice + " means. Try typing a "+a+" or a "+b+". ")
	return choice
	"""
	if choice != a or choice != b:
		choice = input("I don't know what " + choice + " means. Try typing a "+a+" or a "+b+". ")
	else:
		return choice
	"""

def throneRoom():
	checkTime()
	king = input("\n\nThe king is in much distress, but they say he was the last one to see his son before the abduction.\n\nDo you \n1) ask him for clues or \n2) let him grieve in peace and head to the stables?\n\n>> ")

	if checkInput(king, '1', '2') == '1':
		kingClue()
	elif checkInput(king, '1', '2') == '2':
		peaceGrieve()

def stables():
	checkTime()
	stableBoy = input("\n\nThe stable boy is looking for the horse, Misty, that the prince was riding when he was abducted. Misty was last seen at the garden with the prince, who was tending to his favorite sunflower patch. The stable boy seems very sad, as Misty was his favorite horse to take care of. Misty always 'knew the right way to go about things.'\n\nWould you like to\n1) go to the garden or\n2) help the stable boy find Misty?\n\n>> ")
	if checkInput(stableBoy, '1', '2') == '1':
		garden()
	elif checkInput(stableBoy, '1', '2') == '2':
		findMisty()

def findMisty():
	global startTime
	checkTime()
	startTime += 30
	print("\n\nYou spend an hour looking for Misty, while time to save the prince ticks by. Because of your preoccupation with Misty rather than saving the prince, 30 seconds have been deducted from the time you have remaining. Then, a thought occurs to you. The prince could have been abducted along with Misty! After all, the sorceress could have somehow led them through a spell to her lair. You decide that you must go back to the garden and follow the stable boy's original clue.\n\n>> ")
	garden()

def kingClue():
	checkTime()
	clue = input("\n\nMy boy, oh my boy! What will we ever do? He was my pride and joy, that boy. He was so fond of that garden of ours, that he spent every waking minute in it tending to the sunflowers. Not to mention the second thing he was most fond of - his favorite horse, Misty! He always brought her to that garden with him. That wretched sorceress dragged him off because she was jealous of my happiness. Just remember one thing! The sorceress once told me (back when she was a normal person) that 'Right is the way of evil.'\n\nNow that you have gained this clue, do you wish to\n1) go straight to the garden or\n2) talk to the stable boy to gain more clues?\n\n>> ")
	if checkInput(clue, '1', '2') == '1':
		garden()
	if checkInput(clue, '1', '2') == '2':
		stables()

def peaceGrieve():
	checkTime()
	queen = input("\n\nNow that you left the king to grieve in peace, you encounter the queen walking back from her morning walk around the gardens. She tells you that her husband would answer any questions asked to him in this period of grieving because he is determined to find his son and bring him back.\n\nDo you\n1) go back to the throne room to talk to the king or\n2) head to the stables?\n\n>> ")
	if checkInput(queen, '1', '2') == '1':
		throneRoom()
	elif checkInput(queen, '1', '2') == '2':
		stables()

def garden():
	checkTime()
	garden = input("\n\nNow that you have found the sunflowers, you notice something interesting about the sunflowers closest to the forest. It looks like they were trampled by something somehow, maybe a horse. It looks as though the prince went this way! There are two paths into the forest.\n\nDo you go to the\n1) left or the\n2) right? ")
	if checkInput(garden, '1', '2') == '1':
		leftPath()
	elif checkInput(garden, '1', '2') == '2':
		rightPath()

def leftPath():
	checkTime()
	leftChoice = input("\n\nThe path ahead is windy and filled with chilly winds. Knowing that the sorceress has a knack for picking scary places to set up her lair, you are reassured by the state of this path leading you to your destiny.\n\nDo you want to\n1) continue down the left path or\n2) turn back to choose between paths again? ")
	if checkInput(leftChoice, '1', '2') == '1':
		continueLeft()
	elif checkInput(leftChoice, '1', '2') == '2':
		garden()

def continueLeft():
	global startTime
	checkTime()
	startTime += 30
	turnaround = input("\n\nYou walked for quite a while and have now come to a dead end in the road. Looks like you didn't heed the advice you were given very well! 30 seconds have been deducted from the time you have left.\n\nType 1 or 2 to continue back to the two paths. ")
	if checkInput(turnaround, '1', '2') == '1':
		garden()
	elif checkInput(turnaround, '1', '2') == '2':
		garden()

def rightPath():
	checkTime()
	rightChoice = input("\n\nThe path ahead is calm and clear, as hot as a summer day. It definitely doesn't give off the vibe of a path leading to a scary secret lair. But then again, looks are often deceiving.\n\nDo you want to \n1) continue down the right path or\n2) turn back and choose between paths again? ")
	if checkInput(rightChoice, '1', '2') == '1':
		continueRight()
	elif checkInput(rightChoice, '1', '2') == '2':
		garden()

def continueRight():
	checkTime()
	oldman = input("\n\nYou soon happen upon an old wise-looking man, standing as a guard in front of a frought-iron gate. He looks into your eyes and simply says 'The fields of mist contain your key.' Then, he moves aside and the large gates open, revealing an underwater cave on one side and a green pasture on the the other.\n\nDo you choose to\n1) visit the cave or\n2) visit the pasture? ")
	if checkInput(oldman, '1', '2') == '1':
		cave()
	elif checkInput(oldman, '1', '2') == '2':
		pasture()

def pasture():
	checkTime()
	misty = input("\n\nAs you arrive at the pasture, you see the outline of... is that a horse? It's the beloved Misty! You've found her! You get up close and examine her. She is tied to a wooden fence but she seems content with her food. The knot on her rope seems really difficult to untie, and the prince is nowhere to be found on this pasture in the middle of nowhere. Wait! Something suddenly catches your eye about Misty's collar. The collar has the numbers '1029' engraved on it.\n\nNow, you have a choice to either\n1) go explore the cave or\n2) help untie Misty! >> ")
	if checkInput(misty, '1', '2') == '1':
		cave()
	elif checkInput(misty, '1', '2') == '2':
		untieMisty()

def cave():
	checkTime()
	code = input("\n\nYou arrive at the cave, which is underground under a body of water. You snoop around and find two sets of footprints leading to a wall of the cave... yet they suddenly disappear. This definitely looks like the work of magic! Or...is it? You trace your hand down the side of the limestone rock wall and find yourself somehow turning something...something that sounds mechanical. When you peer at what your hand is touching, you see a combination type lock that seems to be accepting four numbers.\n\nDo you\n1) try a four-digit code or\n2) go back to the old gate-keeper? >> ")
	if checkInput(code, '1', '2') == '1':
		unlock()
	elif checkInput(code, '1', '2') == '2':
		continueRight()

def untieMisty():
	global startTime
	checkTime()
	startTime += 30
	untie = input("\n\nYou wrestle with the knot for what seems like hours, but it seems like a spell has been cast on the knot so that any progress you do with undoing the knot, it seems to knot itself back together even worse than before. Pretty soon, poor Misty seems to be in a tangled mess, but she's still happy because she has her favorite snacks by her side. Her collar still prominently reads, '1029'. You, however, just wasted time by not thinking about the prince and thinking about his horse instead. 30 seconds have been deducted from the time you have left. Looks like you will have to go to the cave for now.\n\nType 1 or 2 to continue.\n\n>> ")
	if checkInput(untie, '1', '2') == '1':
		cave()
	elif checkInput(untie, '1', '2') == '1':
		cave()

def unlock():
	checkTime()
	inputCode = input("The lock reads, Enter the 4-digit PIN: ")
	if inputCode == '1029':
		lair()
	else:
		locked = input("Oops! Looks like you didn't put in the right pin code. You'll have to try again or gather more clues. Would you like to 1) return to the old man or 2) try again? ")
		if checkInput(locked, '1', '2') == '1':
			continueRight()
		elif checkInput(locked, '1', '2') == '2':
			unlock()

def lair():
	# no more checking the time, as the prince has been found and the timer is now invalid.
	free = input("\n\nSuddenly, the rock formation shakes and opens its doors. You step inside, and the rock repositions itself. Woah! You feel a sudden drop. When the doors open, you see the prince, face fallen, scrunched up against the side of a large cage. The key is tauntingly in his reach, but he can't seem to get it. The prince suddenly spots you, and brings a finger to his lips to mouth 'Shhh.' You look to the side and find the snoring sorceress, taking an afternoon siesta. You tip-toe over to the prince and use the key to unlock him. You both continue out of the lair, leaving the sorceress to find out the surprise when she wakes up later.\n\nType 1 or 2 to continue. >> ")
	if checkInput(free, '1', '2') == '1':
		exit()
	elif checkInput(free, '1', '2') == '2':
		exit()

def exit():
	leave = input("\n\nYou emerge from the cave and travel to the gates to find the old man standing behind Misty, who has somehow been freed from her predicament. You and the prince ride back to the kingdom to deliver the good news that the prince is safe.\nType a 1 or a 2 to continue.\n\n>> ")
	if checkInput(leave, '1', '2') == '1':
		win()
	elif checkInput(leave, '1', '2') == '2':
		win()

def win():
	wish = input("\n\nWhen you arrive at the kingdom, you are celebrated as a hero. The king and queen are so happy with you that they are willing to grant any wish of yours.\nWhat would you like to wish for?\n\n>> ")
	print("The king and queen say that they can surely make that happen, although no one has ever asked for "+wish+" before. ")
	courting = input("\n\nAfter the festivities, the prince pulls you aside and asks you if you would like to enter a courtship with him, as he can't take his eyes off the brave person who saved him.\n\nDo you say\n1) yes or\n2) no?\n\n>> ")
	if checkInput(courting, '1', '2') == '1':
		playAgain = input("\n\nAww! I just love young love. I wish you a happily ever after. Thank you so much for embarking on this quest with me! Would you like to save the prince again?\nType 1 for yes and 2 for no. ")
		# although this is repeated in the other elif statement, I can't use a method because when I tried that, it seems like the variable playAgain is specific to the win() method
		if checkInput(playAgain, '1', '2') == '1':
			start()
		elif checkInput(playAgain, '1', '2') == '2':
			print("\n\nFarewell, my dear friend. I will miss you.")
	elif checkInput(courting, '1', '2') == '2':
		playAgain = input("\n\nThe prince totally understands. First of all, you don't really know him that well, and second of all, your a strong independent person who don't need no man. Well, it was so great having you along for this quest. Would you like to save the prince again?\nType 1 for yes and 2 for no. ")
		if checkInput(playAgain, '1', '2') == '1':
			start()
		elif checkInput(playAgain, '1', '2') == '2':
			print("\n\nFarewell, my dear friend. I will miss you.")

start()