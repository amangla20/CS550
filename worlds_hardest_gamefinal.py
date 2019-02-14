# https://www.pygame.org/docs/tut/tom_games4.html
import pygame, sys
import math

pygame.init()
height = 500
width = 500
size = [width, height]
balls = []
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World's Hardest Game! Can you beat it in time?")
done = False
time = pygame.time.get_ticks
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

    def oscillate_vertically(self, posy):
    	if self.posy < height:
    		self.posy += 1
    	elif self.posy == height:
    		self.posy -= 1
    	elif self.posy == 0


while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#ball1 = Ball(100, 100)

	posx = int(width/10)
	posy = int(height/5)

	for i in range(5):
		balls.append(posx)
		posx += 100

	for i in range(5):
		ball = Ball(balls[i], posy)
		ball.oscillate_vertical(posy)
		pygame.display.update()
	pygame.display.flip()
pygame.quit()
# hints with text box for each level 






