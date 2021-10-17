print('#intro')
class Dog:
	"""Just attempt to model a dog """
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")				
my_dog.sit()
my_dog.roll_over()


print("\n#9.1")

class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restaurant(self):
		print(f"\nThe restaurant's name is {self.restaurant_name}.")
		print(f"The type of the restaurant's cuisine is {self.cuisine_type}.")

	def open_restaurant(self):
		print(f'The "{self.restaurant_name}" is open!')

new_restaurant = Restaurant('Rainbow', 'some_type')
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

print("\n#9.2")

sunrise = Restaurant('sunrise', 'x')
cow = Restaurant('cow', 'y')
your_kitchen = Restaurant('your kitchen', 'z')

print(sunrise.restaurant_name)
print(sunrise.cuisine_type)
sunrise.describe_restaurant()
sunrise.open_restaurant()
print()
print(cow.restaurant_name)
print(cow.cuisine_type)
cow.describe_restaurant()
cow.open_restaurant()
print()
print(your_kitchen.restaurant_name)
print(your_kitchen.cuisine_type)
your_kitchen.describe_restaurant()
your_kitchen.open_restaurant()

print("\n#9.3")

class User:
	def __init__(self, first_name, last_name, age, status):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.status = status

	def describe_user(self):
		print(f"\nUsername is {self.first_name} {self.last_name}.")
		print(f"Username is {self.age} years old.")
		print(f'Status: {self.status}.')

	def greet_user(self):
		print(f"Hello, {self.first_name}!")

willie = User('Willie', 'Black', 20, '...')
ann = User('Ann', 'White', 25, 'some text')

willie.describe_user()
willie.greet_user()
ann.describe_user()
ann.greet_user()

