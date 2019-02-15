# https://www.pygame.org/docs/tut/tom_games4.html
import pygame, sys
import math
# def oscillate_vertical(posx, posy):
# 	for i in range(height - posy):
# 		ball = Ball(posx, posy)
# 		posy += 1

# class Ball:
# 	def __init__(self, posx, posy):
# 		self.posx = posx
# 		self.posy = posy
# 		pygame.draw.circle(screen, (0, 0, 255), [posx, posy], 5)

# 	def oscillate_vertical(self, posy):
# 		newposy = self.posy + 1
# 		self.__init__(self.posx, newposy)

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, posx, posy):
        super().__init__()
        pygame.draw.circle(screen, (0, 0, 255), [posx, posy], 5)
        self.posx = posx
        self.posy = posy

    def oscillate_vertically(self, posy):
    	self.posy += 1
# Source: https://www.101computing.net/pygame-how-to-control-your-sprite/
class Player(pygame.sprite.Sprite):

	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill((255, 255, 255))
		self.image.set_colorkey((255, 255, 255))

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.rect = self.image.get_rect()

	def moveRight(self, posx):
		self.rect.x += posx

	def moveLeft(self, posx):
		self.rect.x -= posx

	def moveUp(self, posy):
		self.rect.y -= posy

	def moveDown(self, posy):
		self.rect.y += posy

pygame.init()
height_screen = 500
width_screen = 500
size = [width_screen, height_screen]
balls = []
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World's Hardest Game! Can you beat it in time?")
done = False
time = pygame.time.get_ticks

all_sprites_list = pygame.sprite.Group()

player = Player((255, 0, 0), 60, 60)
player.rect.x = 0
player.rect.y = 0

all_sprites_list.add(player)

clock = pygame.time.Clock()

while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		player.moveRight(5)
	if keys[pygame.K_UP]:
		player.moveUp(5)
	if keys[pygame.K_DOWN]:
		player.moveDown(5)

	all_sprites_list.update()
	screen.fill((0, 0, 0))
	ball1 = Ball(100, 100)

	posx = int(width_screen/10)
	posy = int(height_screen/5)

	for i in range(5):
		balls.append(posx)
		posx += 100

	for i in range(5):
		ball = Ball(balls[i], posy)
		ball.oscillate_vertically(posy)
		pygame.display.update()

	all_sprites_list.draw(screen)

	pygame.display.flip()

	clock.tick(60)
pygame.quit()
# hints with text box for each level 






