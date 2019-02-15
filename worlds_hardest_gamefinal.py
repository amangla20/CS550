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

player = Player((255, 0, 0), 25, 25)
player.rect.x = 0
player.rect.y = 0

all_sprites_list.add(player)

# #Day
# DayFont = Font.render("Day:{0:03}".format(Day),1, Black) #zero-pad day to 3 digits
# DayFontR = DayFont.get_rect()
# DayFontR.center=(985,20)
# #Hour
# HourFont = Font.render("Hour:{0:02}".format(Hour),1, Black) #zero-pad hours to 2 digits
# HourFontR=HourFont.get_rect()
# HourFontR.center=(1085,20)
# #Minute
# MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, Black) #zero-pad minutes to 2 digits
# MinuteFontR=MinuteFont.get_rect()
# MinuteFontR.center=(1200,20)

clock = pygame.time.Clock()
clock_tick = pygame.USEREVENT + 1
pygame.time.set_timer(clock_tick, 1000)
# https://stackoverflow.com/questions/38045189/how-do-i-make-pygame-display-the-time-and-change-it-when-the-time-changes-using
while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True
		# if event.type == clock_tick:
		# 	Minute = Minute + 1
		# 	if Minute == 60:
		# 		Hour = Hour + 1
		# 		Minute = 0
		# 	if Hour == 12:
		# 		Day = Day + 1
		# 		Hour = 0
		# 	screen.fill((255, 255, 255))
  #           # redraw time
  #           MinuteFont = Font.render("Minute:{0:02}".format(Minute), 1, Black)
  #           screen.blit(MinuteFont, MinuteFontR)
  #           HourFont = Font.render("Hour:{0:02}".format(Hour), 1, Black)
  #           screen.blit(HourFont, HourFontR)
  #           DayFont = Font.render("Day:{0:03}".format(Day), 1, Black)
  #           screen.blit(DayFont, DayFontR)

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

	# Font = pygame.font.SysFont("Trebuchet MS", 25)


	pygame.display.flip()

	clock.tick(60)
pygame.quit()
# hints with text box for each level 






