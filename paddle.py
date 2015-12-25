# well, this is obnoxious
import pygame

MOVE_UP = 0
MOVE_DOWN = 1

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
		# L/R, T/A, U/D
		# move up, move down
		self.reward = [[-100, -100, -100, -100, 0, 0, 0, 0],
				  [-100, -100, -100, -100, 0, 0, 0, 0]]

		self.Q = [[0, 0, 0, 0, 0, 0, 0, 0],
			 [0, 0, 0, 0, 0, 0, 0, 0]]

		self.gamma = .8 # discount value
		self.alpha = .7 # learning rate
		
		self.oldAction = MOVE_DOWN # arbitrary
		self.oldState = 0
		
		self.ballLeft = False
		self.ballMoveLeft = False
		self.ballMoveUp = False

	def getRewardIndex(self):
		if (self.ballLeft and self.oldState > 3):
			print("here")
		
		# get the index of the Q matrix to reference based on state variables	
		return (not self.ballLeft * 4) + (not self.ballMoveLeft * 2) + (not self.ballMoveUp * 1)

	def getMaxEstimate(self):
		return max(self.Q[MOVE_UP][self.getRewardIndex()], self.Q[MOVE_DOWN][self.getRewardIndex()])

	def updateQMatrix(self):
		newVal = self.Q[self.oldAction][self.oldState] + \
				self.alpha * \
				(self.reward[self.oldAction][self.getRewardIndex()] + \
				self.gamma * self.getMaxEstimate() - \
				self.Q[self.oldAction][self.oldState])
		self.Q[self.oldAction][self.getRewardIndex()] = newVal
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
		self.updateQMatrix()

		# movement logic
		if self.Q[MOVE_UP][self.getRewardIndex()] > self.Q[MOVE_DOWN][self.getRewardIndex()]:
			# move up
			self.rect.move_ip(0, -self.speed)
			self.oldAction = MOVE_UP
		else:
			# move down
			self.rect.move_ip(0, self.speed)
			self.oldAction = MOVE_DOWN
		
		self.oldState = self.getRewardIndex()
