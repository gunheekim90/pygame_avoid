import pygame as pyg
import numpy as np
import random

# initializes all modules required for pyg
pyg.init()

# define the window dimensions
window_length = 300 # can be simplified as 300//50 = 6 columns
window_height = 400 # can be simplified as 400//50 = 8 rows
wall_color = (226,46,46)
player_color = (157,207,199)
enemy_color = (254,0,197)
player_s = 50 # can be simplified as 50//50 = 1 cell
player_x = window_length // 2
player_y = window_height - player_s
clock = pyg.time.Clock()
block_rate = 10
limit_left  = player_s
limit_right = window_length-2*player_s
frame_number = 0
enemy_positions = np.arange(start=limit_left, stop=limit_right+player_s, step=player_s)
enemy_x = np.random.choice(a=enemy_positions)
enemy_y = 0

# return value is a Surface object for graphical operations
screen = pyg.display.set_mode((window_length,window_height))
done = False

def move_player(direction, player_x, player_s):
	if direction == -1:
		return player_x - player_s if player_x > limit_left else player_x
	if direction == 0:
		return player_x
	if direction == 1:
		return player_x + player_s if player_x < limit_right else player_x

def evaluate_pixel_color(position):
	pixel_color = screen.get_at((position[0],position[1]))[0:3]
	if pixel_color == (0,0,0):
		# color of a neutral space
		return 0
	elif pixel_color == (157,207,199):
		# color of a player space
		return 1
	elif pixel_color == (254,0,197):
		# color of an enemy space
		return 2

# compose simplified pixel matrix
# create a simple 1D array representing one column
col_array       = np.arange(start=player_s,stop=(window_length-player_s),step=player_s)
col_array_size  = col_array.size
# create a simple 1D array representing one row
row_array       = np.arange(start=0,stop=window_height,step=player_s)
row_array_size  = row_array.size
# replicate (tile) the simple column array for each row
tiled_col_array = np.tile(col_array,row_array.size)
# replicate (repeat) the simple row array for each column
rep_row_array   = row_array.repeat((window_length-2*player_s)//player_s)
# zip the two replicated arrays into an array of tuples
zipped_array    = list(zip(tiled_col_array,rep_row_array))

while not done:
	# event.get() empties the event queue
	for event in pyg.event.get():
		if event.type == pyg.QUIT:
			done = True

	print("Frame Number (Score): {frame_number}".format(frame_number=frame_number))
	# each turn the enemy block goes down one space
	if enemy_y < window_height:
		enemy_y = enemy_y + player_s
	else:
		enemy_y = 0
		enemy_x = np.random.choice(a=enemy_positions)

	# generate a random player move
	player_x = move_player(random.randint(-1,1), player_x, player_s)
	# fill the screen with black to 'reset' the screen
	screen.fill((0,0,0))
	# draw left boundary of the game screen
	pyg.draw.rect(screen,wall_color, pyg.Rect(0,0,50,window_height))
	# draw right boundary of the game screen
	pyg.draw.rect(screen,wall_color, pyg.Rect(window_length-player_s,0,50,window_height))
	# redraw the player block
	pyg.draw.rect(screen,player_color, pyg.Rect(player_x,player_y,player_s,player_s))
	# redraw the enemy block
	pyg.draw.rect(screen,enemy_color, pyg.Rect(enemy_x,enemy_y,player_s,player_s))
	#increment the frame count
	frame_number += 1

	# map each pixel tuple to the relevant color, and then color code (0~2)
	mapped_list = [evaluate_pixel_color(position) for position in zipped_array]
	# reshape the list into a matrix of the appropriate dimensions and print
	print(np.matrix(mapped_list).reshape(row_array_size,col_array_size))

	# check if enemy and player blocks have merged
	if player_x == enemy_x and player_y == enemy_y:
		print("GAME OVER")
		done = True

	pyg.display.flip()
	# will block execution until 1/block_rate seconds have passed
	clock.tick(block_rate)
