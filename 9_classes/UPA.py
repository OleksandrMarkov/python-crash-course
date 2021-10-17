class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			print("\nPrivileges:")
			for p in self.privileges:
				print(p)		

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

class Admin(User):
	def __init__(self, first_name, last_name, age, status):
		User.__init__(self, first_name, last_name, age, status)
		self.privileges = Privileges(['can add post', 'can ban user'])
