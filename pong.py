# imports.  cuz that's important
import sys
import pygame
import random

from paddle import Paddle
from ball import Ball
from wall import Wall


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
		
	# --------------------	
	# initialization stuff
	# --------------------

	pygame.init()
	screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
	clock = pygame.time.Clock()

	# set up screen.  I do not understand pygame's shenanigans
	bg = pygame.Surface(screen.get_size())
	bg.convert() # not quite sure why this is here...
	bg.fill((0, 0, 0))

	# set up paddle
	paddle = Paddle(P_WIDTH, P_HEIGHT, P_SPEED)

	# set up ball
	ball = Ball(B_SIZE, B_SIZE, B_SPEED)

	# set up wall
	wall = Wall(B_SIZE, S_HEIGHT)

	# render the things
	objects = pygame.sprite.RenderPlain((paddle, ball, wall))

	# random number generator for ball	
	random.seed()

	# ------------------------
	# end initialization stuff
	# ------------------------

	setupEpisode(paddle, ball, wall)
	
	while 1:
		# 'quit logic' in this function
		# run training episodes forever
		setupEpisode(paddle, ball, wall)
		runEpisode(screen, clock, bg, paddle, ball, wall, objects)

	
def setupEpisode(paddle, ball, wall):	
	# paddle
	paddle.rect.x = 20
	paddle.rect.y = S_HEIGHT/2 - P_HEIGHT/2

	# ball	
	ball.dx = B_SPEED
	ball.rect.x, ball.rect.y = S_WIDTH/2, random.randint(S_HEIGHT // 4, (S_HEIGHT * 3) // 4)

	# wall	
	wall.rect.x = S_WIDTH - 20

def runEpisode(screen, clock, bg, paddle, ball, wall, objects):
	# main event loop
	dead = False;
	while not dead:
		# make us not hog the CPU.  arg is fps
		clock.tick(120)
		
		# exit if we quit	
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		# movement logic for paddle in Paddle class

		# collisions for ball
		# clone the rectangle and then move it to test where the ball WILL be
		ballRect = ball.rect.copy()
		ballRect.move_ip(ball.dx, ball.dy)

		if (ballRect.collidelist((paddle.rect, wall.rect)) != -1):
			# flip x velocity if ball hits paddle or wall
			ball.dx *= -1
		
		if (ball.rect.y <= 0) or (ball.rect.y + B_SIZE >= S_HEIGHT):
			# collision with top or bottom of screen	
			ball.dy *= -1
		
		if (ball.rect.x + B_SIZE >= S_WIDTH):
			# collision with right wall
			ball.dx *= -1

		paddle.ballLeft = ball.rect.x < paddle.rect.x
		paddle.ballMoveLeft = ball.dx < 0
		paddle.ballMoveUp = ball.dy < 0
	
		if (ball.rect.x <= 0):
			# got past paddle
			# run new episode
			dead = True;

		# update all sprites
		objects.update()

		# update display
		screen.blit(bg, (0,0)) # don't know why this is here either	
		objects.draw(screen)
		pygame.display.flip() # contents of double buffer
	

main()
