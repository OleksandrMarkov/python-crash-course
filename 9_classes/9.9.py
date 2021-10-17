class Battery:
	def __init__(self, battery_size = 75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kwh battery.")

	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315		
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100

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

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year) # to call method of the superclass
		self.battery = Battery()

	def fill_gas_bank():
		print("This car does not need a gas tank!")

my_car = ElectricCar('tesla', 'model X', 2020)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()		