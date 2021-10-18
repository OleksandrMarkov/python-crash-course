from random import randint

class Die:
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		result = randint(1, self.sides)
		print(f"Result: {result}.")		
