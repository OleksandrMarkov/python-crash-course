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
print()

"""Work with classes and their copies """
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")	

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles			

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()			
my_new_car.increment_odometer(2)
my_new_car.read_odometer()

print("\n#9.4")

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

restaurant = Restaurant('super', 'X')
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)

restaurant.set_number_served(12)
print(restaurant.number_served)

print("\n#9.5")

class User:
	def __init__(self, first_name, last_name, age, status):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.status = status
		self.login_attempts = 0

	def describe_user(self):
		print(f"\nUsername is {self.first_name} {self.last_name}.")
		print(f"Username is {self.age} years old.")
		print(f'Status: {self.status}.')

	def greet_user(self):
		print(f"Hello, {self.first_name}!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

new_user = User('James', 'Hubner', 34, 'no status')
print(new_user.login_attempts)
for i in range(20):
	new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)						