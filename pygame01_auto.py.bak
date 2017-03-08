import pygame

# initializes all modules required for Pygame
pygame.init()

# return value is a Surface object for graphical operations
screen = pygame.display.set_mode((400,300))
done = False

while not done:
	# event.get() empties the event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		pygame.draw.rect(screen,(0,128,255), pygame.Rect(30,30,60,60))
	# required to show updates on the game screen
	pygame.display.flip()
