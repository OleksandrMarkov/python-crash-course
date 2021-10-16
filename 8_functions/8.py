"""it is docstring"""

def	greet_user(username):
	""" Show simple message"""
	print(f"Hello, {username.title()}!")


def	task81():
	""" info about the 8th chapter"""
	print(f"some info")

def favorite_book(book):
	"""task #8.2: my favorite book"""
	print(f"One of my favorite books is {book.title()}.") 

#greet_user('Alex')
#task81()
#favorite_book("bible")

def describe_pet(animal_type, pet_name):
	"""positional arguments"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

def describe_pet2(animal_type, pet_name):
	"""key arguments"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

def describe_pet3(pet_name, animal_type = 'swine'):
#def describe_pet3(animal_type = 'swine', pet_name): is not working	
	"""default parameter value"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')

describe_pet2(animal_type = 'dog', pet_name = 'willie')
# or describe_pet2(pet_name = 'willie', animal_type = 'dog')

describe_pet3('kate')
describe_pet3('tony', 'wolf')

print('\n#8.3')
def make_shirt(size, text):
	""" 8.3"""
	print(f"Shirt's size is {size}. Logo is {text}.")

make_shirt(23, 'sometext')
make_shirt(text = 'sometext', size = 23)	


print('\n#8.4')
def make_shirt2(size = 'L', text = 'I love Python'):
	print(f"Shirt's size is {size}. Logo is {text}.")

make_shirt2()
make_shirt2(size = 'M')
make_shirt2(size = 'XL', text = '...')

print('\n#8.5')
def describe_city(city, country = 'Denmark'):
	print(f"{city.title()} is in {country.title()}.")

describe_city('Copengagen')
describe_city('Paris', 'France')
describe_city(country = 'Ukraine', city = 'ZP')