import pygame

class MovingBlock:
	def __init__(self, surface, posx, posy, width, height, upperlim, lowerlim, speed, kind):
		self.surface = surface
		self.posx = int(posx)
		self.posy = int(posy)
		self.upperlim = int(upperlim)
		self.lowerlim = int(lowerlim)
		self.speed = int(speed)
		self.kind = int(kind)
		self.image = pygame.Surface([width, height])
		self.image.fill((255, 255, 255))
		self.image.set_colorkey((255, 255, 255))

		self.image = pygame.image.load("movingblock.png").convert_alpha()

		self.rect = self.image.get_rect()
		screen.blit(self.image, (self.posx, self.posy))

	def oscillate_direction(self):
		if self.kind == 1:
			self.oscillate_vertical()
		elif self.kind == 2 or self.kind == 3:
			self.oscillate_horizontal()	

	def oscillate_vertical(self):
			if self.posy >= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posy <= self.upperlim:
				self.speed = -1 * self.speed
			newposy = self.posy + self.speed

			self.__init__(self.surface, self.posx, newposy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

	def oscillate_horizontal(self):
			if self.posx <= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posx >= self.upperlim:
				self.speed = -1 * self.speed
			newposx = self.posx + self.speed

			self.__init__(self.surface, newposx, self.posy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

