class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 0

	def describe_restaurant(self):
		print(f"\nThe restaurant's name is {self.restaurant_name}.")
		print(f"The type of the restaurant's cuisine is {self.cuisine_type}.")

	def open_restaurant(self):
		print(f'The "{self.restaurant_name}" is open!')

	def set_number_served(self, new_customers):
		self.number_served += new_customers


class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		Restaurant.__init__(self, restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors(self):
		if self.flavors:
			print("\nFlavors: ")	
			for f in self.flavors:
				print(f)	

ice1 = IceCreamStand('res1', 'cuis1', ['f1', 'f2', 'f3'])
ice1.show_flavors()