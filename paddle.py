# well, this is obnoxious
import pygame

MOVE_UP = 0
MOVE_DOWN = 1
STAY = 2

class Paddle(pygame.sprite.Sprite):

	# Constructor	
	def __init__(self, width, height, inspeed):
		# default sprite init method
		pygame.sprite.Sprite.__init__(self)

		# draw the block for the ball
		self.image = pygame.Surface((width, height))
		self.image.fill((255, 255, 255))

		# bounding rectangle for collisions and stuff	
		self.rect = self.image.get_rect()

		self.speed = inspeed;

		# ----------------------
		# Q LEARNING SHENANIGANS
		# ----------------------

		# Reward matrix
		# >> Ball to the left/right of the paddle
		# >> Ball moving left/right
		# >> Ball above/below the paddle
		# move up, move down
		# penalize less for trying to do the right thing?
		self.reward =	[[0, -100, 0, -100, 0, 0, 0, 0],
				  	   	[-100, 0, -100, 0, 0, 0, 0, 0],
						[-100, -100, -100, -100, 0, 0, 0, 0]]

		self.Q = 	[[0, 0, 0, 0, 0, 0, 0, 0],
			 		[0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0]]

			
		self.alpha = .5 # learning rate
		self.gamma = .8 # discount value
		
		self.oldAction = MOVE_DOWN # arbitrary
		self.oldState = 0
		
		self.ballLeft = False
		self.ballMoveLeft = False
		self.ballAbove = False

	def getRewardIndex(self):
		# get the index of the Q matrix to reference based on state variables
		# parentheses are important
		return ((not self.ballLeft) * 4) + \
				((not self.ballMoveLeft) * 2) + \
				((not self.ballAbove) * 1)

	def getMaxEstimate(self):
		# the max Q for our current state
		return max(self.Q[MOVE_UP][self.getRewardIndex()], self.Q[MOVE_DOWN][self.getRewardIndex()])

	def updateQMatrix(self):
		newVal = self.Q[self.oldAction][self.oldState] + \
				self.alpha * \
				(self.reward[self.oldAction][self.oldState] + \
				self.gamma * self.getMaxEstimate() - \
				self.Q[self.oldAction][self.oldState])
		self.Q[self.oldAction][self.oldState] = newVal
		# self.Q[self.oldAction][self.oldState] = newVal


	def update(self):
		""" MANUAL CONTROL
		if keys[pygame.K_UP]:
			self.rect.move_ip(0, -self.speed)
		elif keys[pygame.K_DOWN]:
			self.rect.move_ip(0, self.speed)
		"""
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			print(self.Q)

		# update Q matrix
		# do this before our next action so it's like we're updating for the action we just took
		# self.updateQMatrix()

		# movement logic
		if self.Q[MOVE_UP][self.getRewardIndex()] > self.Q[MOVE_DOWN][self.getRewardIndex()]:
			# move up
			self.rect.move_ip(0, -self.speed)
			self.oldAction = MOVE_UP
		elif self.Q[MOVE_UP][self.getRewardIndex()] < self.Q[MOVE_DOWN][self.getRewardIndex()]:
			# move down
			self.rect.move_ip(0, self.speed)
			self.oldAction = MOVE_DOWN
		else
			# stay still
			self.oldAction = STAY
		
		self.oldState = self.getRewardIndex()
