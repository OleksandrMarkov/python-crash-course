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

def return_full_name(first_name, last_name):
	"""return full_name"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = return_full_name('test', 'testoff')
print(musician)

def return_full_name2(first_name, last_name, middle_name =''):
	"""return full_name"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

return_full_name2('jimmi', 'hendrix')
return_full_name2('john', 'hooker', 'lee')

def build_person(first_name, last_name):
	""" this function returns a dictionary"""
	person = {'first': first_name, 'last': last_name}
	return person

some_guy = build_person('test', 'testoff')
print(some_guy)

def build_person2(first_name, last_name, age = None):
	""" this function returns a dictionary"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

some_guy = build_person2('test', 'testoff', 25)
print(some_guy)


"""meeting with possibility to quit"""
#while True:
#	print('\nPlease tell me your name:')
#	print("(enter 'q' at any time to quit)")

#	f_name = input("First name: ")
#	if f_name == 'q':
#		break

#	l_name = input("Last name: ")
#	if l_name == 'q':
#		break
#	full_name = return_full_name(f_name, l_name)	
#	print(f"Hello, {full_name}")

print('\n#8.6')

def city_country(city, country):
	result = f"{city}, {country}"
	return result

c1 = city_country(city = "Kiev", country = "Ukraine")
c2 = city_country(city = "Minsk", country = "Belarus")
c3 = city_country(city = "Moscow", country = "Russia")

print(c1, c2, c3, sep = "|")	

print('\n#8.7')

def make_album(musician, album):
	result = {'musician' : musician, 'album': album}
	return result

album1 = make_album('tsoy', 'black')
album2	= make_album('mus1', 'alb1')
album3	= make_album('mus2', 'alb2')

print(album1)
print(album2)
print(album3)

def make_album2(musician, album, songs_amount = None):
	result = {'musician' : musician, 'album': album}
	if songs_amount:
		result['songs_amount'] = songs_amount
	return result

album4 = make_album2('mus2', 'alb2', 234)
print('\n', album4)

#while True:
#	print("\nPlease tell me musician's name and album's title: ")
#	print("(Enter 'q' to quit)")
#	mus = input("Musician: ")
#	if mus == 'q':
#		break
#	alb = input("Album: ")	
#	if alb == 'q':
#		break	
#	new_album = make_album(mus, alb)
#	print(new_album)

#function_name(list_name) # list will be mutable
#function_name(list_name[:]) # list will be immutable
#(precisely speaking, we send list's copy)


print("\n# 8.9")
lst = ['msg1', 'msg2', 'msg3', 'msg4', 'msg5']

def show_messages(lst):
	for msg in lst:
		print(msg)

show_messages(lst)

print("\n# 8.10")

def send_messages(lst):
	sent_messages = []
	while lst:
		tmp_msg = lst.pop()
		print(tmp_msg)
		sent_messages.append(tmp_msg)
		
	print("\nMessages: ")
	for msg in lst:
		print(msg)

	print("\nSent messages: ")
	for msg in sent_messages:
		print(msg)

send_messages(lst)


print("\n# 8.11")
lst = ['msg1', 'msg2', 'msg3', 'msg4', 'msg5']

def send_messages2(lst):
	sent_messages = []
	while lst:
		tmp_msg = lst.pop()
		print(tmp_msg)
		sent_messages.append(tmp_msg)		
	print("\nSent messages: ")
	for msg in sent_messages:
		print(msg)

send_messages2(lst[:])
print("\nMessages: ")
for msg in lst:
	print(msg)

def make_pizza(*toppings):
	""" arbitrary number of arguments (must be in the end parameters list)"""
	for t in toppings:
		print(f"- {t}")

make_pizza('t1')
make_pizza('t2', 't3', 't4')
print()

# arbitrary key arguments
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last

	return user_info

user_profile = build_profile('albert', 'einstein',
field = 'physics', location = 'princeton')

print(user_profile)

print("\n# 8.12")
def make_sandwich(*ingredients):
	print("\nMaking a sandwich with following ingredients: ")
	for i in ingredients:
		print(f"- {i}")

make_sandwich('i1', 'i2')
make_sandwich('i3', 'i4', 'i5')

print("\n# 8.13")

def build__my_profile(first, last, **my_info):
	my_info['first_name'] = first.title()
	my_info['last_name'] = last.title()
	return my_info

my_profile = build__my_profile('alex', 'markov', age = 22, iq = 122,
favorite_book = 'bible'.title())

print(my_profile)

print("\n# 8.14")