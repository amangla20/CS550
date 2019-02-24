# import pygame package
import pygame
# class CreateBall creates the ball object (which can also create the moving blocks so it is extremely versatile as a game object class) and initializes the surface, x and y coordinates of the center of the ball or top left corner of the moving block, the upper and lower limits of oscillation, the speed, the kind (1, 2, 3 being balls and 4 and 5 being moving blocks) and the color of the ball object.
class CreateBall:
	# constructor for the CreateBall class initializes the attributes of the ball object as well as draws a white rectangle for moving blocks, a blue circle for the oscillating blue balls, and a yellow ball for the coins.
	def __init__(self, surface, posx, posy, upperlim, lowerlim, speed, kind, rcolor, gcolor, bcolor):
		self.surface = surface
		self.posx = int(posx)
		self.posy = int(posy)
		self.upperlim = int(upperlim)
		self.lowerlim = int(lowerlim)
		self.speed = int(speed)
		self.kind = int(kind)
		self.rcolor = int(rcolor)
		self.gcolor = int(gcolor)
		self.bcolor = int(bcolor)
		# moving block
		if self.kind == 4 or self.kind == 5:
			self.image = pygame.draw.rect(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy, 75, 75])
		# balls/coins
		else:
			self.image = pygame.draw.circle(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy], 5)


	# def display(self, posx, posy, rcolor, gcolor, bcolor):
	# 	for piece in self.balls:
	# 		if piece.kind == "1":
	# 			pygame.draw.circle(self.surface, (int(rcolor), int(gcolor), int(bcolor)), [int(piece.posx), int(newposy)], 5)
	# oscillate either vertically or horizontally
	def oscillate_direction(self):
		if self.kind == 1 or self.kind == 4:
			self.oscillate_vertical()
		elif self.kind == 2 or self.kind == 3 or self.kind == 5:
			self.oscillate_horizontal()	
	# oscillate vertically
	def oscillate_vertical(self):
		# constraints on y position based on upper and lower limits
			if self.posy >= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posy <= self.upperlim:
				self.speed = -1 * self.speed
			# add the "speed" every time the loop runs to increment the y position
			newposy = self.posy + self.speed
			# redraw the ball object
			self.__init__(self.surface, self.posx, newposy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)
	# oscillate horizontally
	def oscillate_horizontal(self):
		# constraints on y position based on upper and lower limits
			if self.posx <= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posx >= self.upperlim:
				self.speed = -1 * self.speed
			# add the "speed" every time the loop runs to increment the y position
			newposx = self.posx + self.speed
			# redraw the ball object
			self.__init__(self.surface, newposx, self.posy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)
