import json

def get_stored_number():
	filename = 'number.json'
	try:
		with open(filename) as f:
			number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return number			

def get_favorite_number():
	number = input("Favorite number? ")
	filename = 'number.json'
	with open(filename, 'w') as f:
		json.dump(number, f)
	return number	 

def greet_user():
	number = get_stored_number()
	if number:
		print(f"Your favorite number is {number}!")
	else:
		number = get_favorite_number()

greet_user()