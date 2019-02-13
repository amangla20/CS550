import pygame
import math

pygame.init()
height = 500
width = 500
size = [width, height]
balls = []
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World's Hardest Game! Can you beat it in time?")
done = False
def oscillate_vertical(posx, posy):
	for i in range(height - posy):
		ball = Ball(posx, posy)
		posy += 1
class Ball:
	def __init__(self, posx, posy):
		self.posx = posx
		self.posy = posy
		pygame.draw.circle(screen, (0, 0, 255), [posx, posy], 5)

	def oscillate_vertical(self, posy):
		for i in range(height - posy):
			self.posy = posy
			posy += 1
			return posy

while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	#ball1 = Ball(100, 100)
	posx = int(width/10)
	posy = int(height/5)
	for i in range(5):
		balls.append(posx)
		posx += 100

	for i in range(5):
		oscillate_vertical(balls[i], posy)




	pygame.display.flip()
pygame.quit()
# hints with text box for each level 






