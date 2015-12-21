# imports.  cuz that's important
from graphics import *

# window dimensions
W_HEIGHT = 400
W_WIDTH = 600

# paddle properties
P_HEIGHT = 80
P_WIDTH = 10
P_SPEED = 10

# ballz
B_SIZE = 10
B_SPEED = 1

# frame
FRAME = 30


def main():	
	print("Initializing pong!");
	
	win = GraphWin("Pong", W_WIDTH, W_HEIGHT)
	win.setBackground("#000000")

	# create the wall (single player)	
	wall = Rectangle(Point(10, 0), Point(10, W_HEIGHT))
	wall.setOutline("#FFFFFF")
	wall.draw(win)

	# create the paddle
	paddle = Rectangle(Point(W_WIDTH - 40 - P_WIDTH, W_WIDTH/2 - P_HEIGHT/2), Point(W_WIDTH - 40, W_WIDTH/2 + P_HEIGHT/2))
	paddle.setFill("#FFFFFF")
	paddle.setOutline("#FFFFFF")
	paddle.draw(win)

	# create the ball
	ball = Rectangle(Point(W_WIDTH/2 - B_SIZE/2, W_HEIGHT/2 - B_SIZE/2), Point(W_WIDTH/2 + B_SIZE/2, W_HEIGHT/2 + B_SIZE/2))
	ball.setFill("#FFFFFF")
	ball.setOutline("#FFFFFF")
	ball.draw(win)
	
	key = ''
	balldx = B_SPEED
	balldy = B_SPEED
	while key != 'q':
		# get the key being pressed	
		key = win.getCurrKey()

		# move paddle appropriately
		if key == 'Up':
			paddle.move(0, -P_SPEED)
		elif key == 'Down':
			paddle.move(0, P_SPEED)

		# check collisions and move ball
		# print(ball.getX())
		ball.move(balldx, balldy)
	
	# input("press [ENTER] to exit")
	win.close()


main()
