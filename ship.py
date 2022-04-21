import pygame

class Ship:
	"""class to handle the ship"""
	def __init__(self, ai_game):
		"""Initialize the ship and set its initial position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# load the ship image and get its attribute 'rect'
		self.image = pygame.image.load('img/ship.bmp')
		self.rect = self.image.get_rect()

		# create every new ship in the screen midbottom	
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""draw the ship in its current position"""
		self.screen.blit(self.image, self.rect)	