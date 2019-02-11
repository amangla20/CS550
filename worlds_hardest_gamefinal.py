import pygame
import math

pygame.init()
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World's Hardest Game! Can you beat it in time?")
done = False
class Ball:
	def __init__(self, posx, posy):
		self.posx = posx
		self.posy = posy
		shape = pygame.draw.circle(screen, (0, 0, 255), [posx, posy], 50)
		return shape

while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	ball1 = Ball(100, 100)
pygame.quit()
# hints with text box for each level 






