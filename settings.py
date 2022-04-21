class Settings:
	"""Class to save all game settings"""
	def __init__(self):
		"""initialize game settings """
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# ship settings
		self.ship_speed = 1.5