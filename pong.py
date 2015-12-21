# imports.  cuz that's important
import sys
import pygame

from paddle import Paddle
from ball import Ball


# window dimensions
S_HEIGHT = 400
S_WIDTH = 600

# paddle properties
P_HEIGHT = 80
P_WIDTH = 10
P_SPEED = 5

# ballz
B_SIZE = 10
B_SPEED = 10

# frame
FRAME = 30


def main():	
	print("Initializing pong!");

	# initialize pygame window and 'globals'
	pygame.init()
	screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
	clock = pygame.time.Clock()

	# set up screen.  I do not understand pygame's shenanigans
	bg = pygame.Surface(screen.get_size())
	bg.convert() # not quite sure why this is here...
	bg.fill((0, 0, 0))

	# set up paddle
	paddle = Paddle(P_WIDTH, P_HEIGHT, P_SPEED)
	paddle.rect.x = 20
	paddle.rect.y = S_HEIGHT/2 - P_HEIGHT/2

	# set up ball
	ball = Ball(B_SIZE, B_SIZE, B_SPEED)
	ball.rect.x, ball.rect.y = S_WIDTH/2, S_HEIGHT/2
	
	# render the things
	objects = pygame.sprite.RenderPlain((paddle, ball))
	

	# main event loop
	while 1:
		# make us not hog the CPU.  arg is fps
		clock.tick(30)
		
		# exit if we quit	
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		# movement logic for paddle in Paddle class

		# collisions for ball
		# eventually gonna have to do a rect clone for the next position, i think...
		if (ball.rect.colliderect(paddle.rect)):
			# flip x velocity if ball hits paddle or wall
			ball.dx *= -1
		if (ball.rect.y <= 0) or (ball.rect.y + B_SIZE >= S_HEIGHT):
			ball.dy *= -1
		if (ball.rect.x + B_SIZE >= S_WIDTH):
			ball.dx *= -1

		# update all sprites
		objects.update()

		# update display
		screen.blit(bg, (0,0)) # don't know why this is here either	
		objects.draw(screen)
		pygame.display.flip()
	
	# input("press [ENTER] to exit")
	win.close()


main()
