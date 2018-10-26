# making a dog class. Think about properties, attributes, other things.

class Dog:
	# constructor
	# scale out of 10
	def __init__(self, name, energy, hunger):
		# listing out properties and giving them initial values
		self.hunger = hunger
		self.energy = energy
		self.happiness = 5
		self.name = name
		# self.name is the property that belongs to the class, while name is the value associated

		# methods/functions

	def play(self):
		if self.energy > 0 and self.hunger > 0:
			self.happiness += 1
			self.hunger -= 1
			self.energy -= 1
			status = self.name + " played and it was fun."
		else: 
			status = "Erm, " + self.name + " needs to not play right now. Maybe try a nap or some food?"
		return status

	def nap(self):
		if self.hunger > 0 and self.energy < 5:
			self.happiness -= 1
			self.hunger -= 1
			self.energy += 2
			status = self.name + " took a nap and is now well rested!"
		else:
			status = "You're dog has too much energy to sleep right now. Maybe try playing with it?"
		return status

	def feed(self):
		if self.hunger < 10:
			self.hunger += 1
			self.happiness += 1
			self.energy += 1
			status = self.name + " ate some dog treats for lunch."
		else:
			status = "You're dog is too full to eat more. Try tiring it out by playing with it!"
		return status

	def stats(self):
		info = "Name: " + self.name
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nHunger: " + str(self.hunger)
		return info

dog1 = Dog("Tetris", 8, 2)
dog2 = Dog("Bat", 5, 7)
# print(dog1.name)
# print(dog1.stats())
# print(dog2.stats())

# dog1.play()
# dog2.play()
# dog1.play()

# print(dog1.stats())
# print(dog2.stats())

while True:
	print(dog1.stats())
	choice = input("What would you like to do with your dog? ")
	if choice == "play":
		print(dog1.play())
	elif choice == "nap":
		print(dog1.nap())
	elif choice == "feed":
		print(dog1.feed())
	elif choice == "nothing":
		print("Are you done caring for your dog already? OK. ")
		break
	else:
		print("You can't do that.")
