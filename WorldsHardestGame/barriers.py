# import package for pygame, csv, and import the Create class from init_barrier.py in order to access getter and setter functions
import pygame
import csv
from init_barrier import Create

# Barriers class makes and displays the barriers/walls that are colored purple, green, or black on the background
class Barriers():
	# constructs the barrier/wall arrangement by taking in the surface and making a barriers list and taking in values from a csv file called barriers.csv which contains the parameters for walls in each column 
	def __init__(self, surface):
		super().__init__()
		self.surface = surface
		self.barriers = []
		with open('barriers.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.barriers.append(Create(row[0], row[1], row[2], row[3], row[4]))
			
	# use the getters and setters from init_barrier to, based on the kind of wall (1 = purple, 2 = black, 3 = green safe space) display the wall by getting the values of csv file that specifies the dimensions for that specific wall
	def display(self, choice):
		if choice == False:
			for location in self.barriers:
				if location.getKind() == 1: #purple walls
					pygame.draw.rect(self.surface, (255, 100, 255), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

		else:
			for location in self.barriers:
				if location.getKind() == 2: #black space
					pygame.draw.rect(self.surface, (0,0,0), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

				elif location.getKind() == 3: 
					#green safe space
					pygame.draw.rect(self.surface, (171, 254, 171), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))