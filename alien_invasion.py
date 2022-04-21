import sys

import pygame

class AlienInvasion:
	"""Class that manages the resources and behavior of the game"""
	
	"""Game initialization, resource creation"""
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230,230,230) # set background color


	def run_game(self):
		""" Start main game loop"""
		while True:
			"""watch the events """
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				""" redraw the screen again on every iteration """		
				self.screen.fill(self.bg_color)			
			"""show last drawn screen"""		
			pygame.display.flip()

if __name__ == '__main__':
	# create an instance and run the game
	ai = AlienInvasion()
	ai.run_game()							