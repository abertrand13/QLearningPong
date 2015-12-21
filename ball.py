import pygame

class Ball(pygame.sprite.Sprite):

	# Constructor
	def __init__(self, width, height, speed):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((width, height))
		pygame.draw.circle(self.image, (255, 255, 255), (width//2, height//2), width//2) # int division

		self.rect = self.image.get_rect()

		self.dx = speed
		self.dy = speed


	def update(self):
		self.rect.move_ip(self.dx, self.dy)

