import pygame

class Ship:
	"""class to handle the ship"""
	def __init__(self, ai_game):
		"""Initialize the ship and set its initial position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		self.screen_rect = ai_game.screen.get_rect()

		# load the ship image and get its attribute 'rect'
		self.image = pygame.image.load('img/ship.bmp')
		self.rect = self.image.get_rect()

		# create every new ship in the screen midbottom	
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)

		# motion indicator
		self.moving_right = False
		self.moving_left = False

	"""Update current ship position"""
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			#self.rect.x += 1
		if self.moving_left and self.rect.left > 0:
			#self.rect.x -= 1
			self.x -= self.settings.ship_speed

		
		self.rect.x = self.x	

	def blitme(self):
		"""draw the ship in its current position"""
		self.screen.blit(self.image, self.rect)	