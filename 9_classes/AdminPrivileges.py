from User import User

class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			print("\nPrivileges:")
			for p in self.privileges:
				print(p)

class Admin(User):
	def __init__(self, first_name, last_name, age, status):
		User.__init__(self, first_name, last_name, age, status)
		self.privileges = Privileges(['can add post', 'can ban user'])				