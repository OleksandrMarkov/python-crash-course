import sys

import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Class that manages the resources and behavior of the game"""
	
	"""Game initialization, resource creation"""
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		# full screen
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

		self.bg_color = (230,230,230) # set background color

	def run_game(self):
		""" Start main game loop"""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()

			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
			#print(len(self.bullets))		

			self._update_screen()

	def _check_events(self):
		"""watch the events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# keydown event	
			elif event.type == pygame.KEYDOWN: 
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)	

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			# move right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# move left
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()				
	
	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):	
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)	

	def _update_screen(self):
		"""update the image on screen and switch to new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		"""show last drawn screen"""		
		pygame.display.flip()

if __name__ == '__main__':
	# create an instance and run the game
	ai = AlienInvasion()
	ai.run_game()						