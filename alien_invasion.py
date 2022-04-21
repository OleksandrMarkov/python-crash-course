import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
	"""Class that manages the resources and behavior of the game"""
	
	"""Game initialization, resource creation"""
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

		self.bg_color = (230,230,230) # set background color

	def run_game(self):
		""" Start main game loop"""
		while True:
			self._check_events()	
			self._update_screen()

	def _check_events(self):
		"""watch the events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""update the image on screen and switch to new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
			
		"""show last drawn screen"""		
		pygame.display.flip()

if __name__ == '__main__':
	# create an instance and run the game
	ai = AlienInvasion()
	ai.run_game()						