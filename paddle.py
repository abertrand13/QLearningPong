# well, this is obnoxious
import pygame

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



	def update(self):
		""" MANUAL CONTROL
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.rect.move_ip(0, -self.speed)
		elif keys[pygame.K_DOWN]:
			self.rect.move_ip(0, self.speed)
		"""
		


