import pygame
import numpy
import random

# initializes all modules required for Pygame
pygame.init()

# define the window dimensions
window_length = 300
window_height = 400
wall_color = (226,46,46)
player_color = (157,207,199)
player_s = 50
player_x = window_length // 2
player_y = window_height - player_s

x = window_length // 2
y = window_height - player_s

clock = pygame.time.Clock()
block_rate = 10
limit_left  = player_s
limit_right = window_length - player_s*2
frame_number = 0
enemy_positions = numpy.arange(start=limit_left, stop=limit_right, step=player_s)
enemy_x = numpy.random.choice(a=enemy_positions)
enemy_y = 0
is_blue = True

# return value is a Surface object for graphical operations
screen = pygame.display.set_mode((window_length,window_height))
done = False

#this is for qutomatic user move
def move_player(direction, player_x, player_s):
	if direction == -1:
		return player_x - player_s if player_x > limit_left else player_x
	if direction == 0:
		return player_x
	if direction == 1:
		return player_x + player_s if player_x < limit_right else player_x

while not done:
	# event.get() empties the event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_blue = not is_blue
	#this is for manually user move 
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT]: 
		x -= player_s if x > limit_left else x
	if pressed[pygame.K_RIGHT]: 
		x += player_s if x < limit_right else x

	print("Frame Number (Score): {frame_number}".format(frame_number=frame_number))
	# each turn the enemy block goes down one space
	if enemy_y < window_height:
		enemy_y = enemy_y + player_s
	else:
		enemy_y = 0
		enemy_x = numpy.random.choice(a=enemy_positions)

	# generate a random player move
	player_x = move_player(random.randint(-1,1), player_x, player_s)
	# fill the screen with black to 'reset' the screen
	screen.fill((0,0,0))
	# draw left boundary of the game screen
	pygame.draw.rect(screen,wall_color, pygame.Rect(0,0,50,window_height))
	# draw right boundary of the game screen
	pygame.draw.rect(screen,wall_color, pygame.Rect(window_length-player_s,0,50,window_height))
	# redraw the player block
	pygame.draw.rect(screen,player_color, pygame.Rect(x,y,player_s,player_s))
	# redraw the enemy block
	pygame.draw.rect(screen,wall_color, pygame.Rect(enemy_x,enemy_y,player_s,player_s))
	#increment the frame count
	frame_number += 1

	# check if enemy and player blocks have merged
	#if player_x == enemy_x and player_y == enemy_y:
	#	print("GAME OVER")
	#	done = True

	if x == enemy_x and y == enemy_y:
		print("shit game is over")
		done = True

	pygame.display.flip()
	# will block execution until 1/block_rate seconds have passed
	clock.tick(block_rate)
