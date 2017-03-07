import pygame

# initializes all modules required for Pygame
pygame.init()

# define the window dimensions
window_length = 400
window_height = 300
wall_color = (226,46,46)
player_color = (157,207,199)
player_s = 50
player_x = window_length // 2 - player_s // 2
player_y = window_height - player_s

# return value is a Surface object for graphical operations
screen = pygame.display.set_mode((window_length,window_height))
done = False

pygame.draw.rect(screen,wall_color, pygame.Rect(0,0,50,window_height))
pygame.draw.rect(screen,wall_color, pygame.Rect(window_length-50,0,50,window_height))

while not done:
	# event.get() empties the event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		pygame.draw.rect(screen,player_color, pygame.Rect(player_x,player_y,player_s,player_s))

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: print("UP BUTTON PRESSED")
	# required to show updates on the game screen
	pygame.display.flip()
