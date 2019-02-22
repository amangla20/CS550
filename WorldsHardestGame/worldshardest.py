import pygame, sys
from barriers import Barriers
from init_balls import CreateBall
import csv
from player2 import Player
import math

pygame.display.init()
Clock = pygame.time.Clock()
#print(pygame.font.get_fonts())
surface = pygame.display.set_mode((677,446))
death = 0
coins = 0
done = False
noMoveRight = False
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(677,446))
rect = background.get_rect()
rect = rect.move((0,0))
surface.blit(background,rect)

wall = Barriers(surface)
wall.display()
def load_balls():
	balls = []
	with open('balls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			balls.append(CreateBall(surface, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
			#print(row)
	return balls


balls = load_balls()


#all_sprites_list = pygame.sprite.Group()
#player = Player(surface, background, (255, 0, 0), 15, 15)
player = Player(surface, background, 75, 373, (255,0,0),15,15)
# player.rect.x = 0
# player.rect.y = 0
#all_sprites_list.add(player)

def loadBackground():
	surface.blit(background, rect)
	wall.display()
	# player = Player(surface, background, 75, 373, (255,0,0),15,15)
	surface.blit(background, player.image, player.image)
	# load_balls()
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()


def collision_detection():
	global death
	global coins
	for ball in balls:
		# position of bottom right corner of player is (posx + 15, posy + 15)
		# center of player is (posx + 7.5, posy + 7.5)
		if math.sqrt(((player.posx+7.5)- ball.posx)**2 + ((player.posy+7.5) - ball.posy)**2) < 12:
			print(ball.kind)
			if ball.kind == 1 or ball.kind == 2:
				death += 1
				coins = 0
				player.posx = 75
				player.posy = 373
				loadBackground()
				#player.posx = 75
				#player.posy = 373
			elif ball.kind == 3:
				coins += 1
				#balls.remove(ball)

def wall_collision():
	for barrier in wall.barriers:
		print(int(barrier.getPosx()))
		if barrier.getKind() == 1:
			if int(barrier.getPosx()) == player.posx:
				noMoveRight = True

# def text_display(message, posx, posy, color):
# 	text_font = pygame.font.SysFont("comicsansms", 10)
# 	text = text_font.render(message, True, color)
# 	text_rect = text.get_rect()
# 	text_rect.center = (posx, posy)
# 	screen.blit(text, text_rect)


while not done:
	print(death)
	print(coins)
	#wall.display()
	collision_detection()
	wall_collision()
	# text_display("Deaths: " + str(death), 30, 10, (0, 0, 0))
	# font = pygame.font.SysFont("comicsansms", 20)
	# death_text = font.render("hey", True, (0, 0, 0))
	# death_rect = death_text.get_rect()
	# death_rect.center = (x + (w/2), (y + (h/2)))
	# surface.blit(death_text, death_rect)
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
		
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		#if player.rect.x > 0:
		if player.posx>0:
			surface.blit(background, player.image, player.image)
			player.moveLeft(5)

	if keys[pygame.K_RIGHT]:
		#if player.rect.x < 677 - player.rect.width:
		if player.posx < 677 - player.width:
			if noMoveRight == False:
				surface.blit(background, player.image, player.image)
				player.moveRight(5)
			else:
				pass

	if keys[pygame.K_UP]:
		#if player.rect.y > 0:
		if player.posy > 0:
			surface.blit(background, player.image, player.image)
			player.moveUp(5)

	if keys[pygame.K_DOWN]:
		#if player.rect.y < 446 - player.rect.height:
		if player.posy < 446 - player.height:
			surface.blit(background, player.image, player.image)
			player.moveDown(5)

	

	#all_sprites_list.update()

	msElapsed = Clock.tick(20)
	pygame.display.flip()