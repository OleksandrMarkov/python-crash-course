print('# introduction')
print()

d1 = {'color': 'green', 'points': 5,}

print(d1)
print()

d1['x'] = 0
d1['y'] = 20

print(d1)
print()

del d1['x']

print(d1)
print()

# instead of d1[price] if you do not sure that 'price' key exists
price = d1.get('price', 'This dictionary has no key "price"!')
print(price)

print('#6.1')
print()

friend = {'first_name' : 'Max', 'last_name' : 'Kennedy', 'age': 30, 'city': 'Virginia'}
print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])

print('#6.2')
print()

favorite_numbers = {'Jack': 100, 'Alex': 1, 'Tom': 23, 'Alice': 2, 'Ann':60}
print(favorite_numbers['Jack'])
print(favorite_numbers['Alex'])
print(favorite_numbers['Tom'])
print(favorite_numbers['Alice'])
print(favorite_numbers['Ann'])

# 6.3 is boring ;)

for key, value in favorite_numbers.items():
	print(f"The favorite number of {key} is {value}.")

for name in favorite_numbers.keys():
	print(name)
# the same result
print()
for name in favorite_numbers:
	print(name)

print()
# sorted keys 
for name in sorted(favorite_numbers.keys()):
	print(f'\n{name} : {favorite_numbers[name]}')

print()

for num in favorite_numbers.values():
	print(num)

print()
# to take values without duplicates:
for num in set(favorite_numbers.values()):
	print(num)


simple_set = {1,2,3,4,5,12,4,34,54}
print(simple_set)

#6.4 is boring :)

print('#6.5')
print()

rivers = {'dnipro':'ukraine', 'mississippi': 'usa', 'amazonas': 'peru'}

for river, country in rivers.items():
	print(f'The {river.title()} runs through {country.title()}')

for river in rivers:
	print(river.title())

print()

for country in rivers.values():
	print(country.title())			

print()
print('#6.6')
print()

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

people = ['edward', 'mike', 'phil', 'ann', 'kate']

for person in people:
	if person in favorite_languages.keys():
		print(f'Thank you, {person.title()}, for taking poll!')
	else:
		print(f'{person.title()}, please, take our poll!')	

print()
print('#6.7')
print()

friend1 = {'first_name' : 'Max', 'last_name' : 'Fischer', 'age': 30, 'city': 'Virginia'}
friend2 = {'first_name' : 'Tom', 'last_name' : 'Thompson', 'age': 20, 'city': 'Oklahoma'}
friend3 = {'first_name' : 'Jane', 'last_name' : 'Kennedy', 'age': 25, 'city': 'Arkansas'}

people = [friend1, friend2, friend3]

for p in people:
	print(f"\nFirst name: {p['first_name']}")
	print(f"Last name: {p['last_name']}")
	print(f"Age: {p['age']}")
	print(f"City: {p['city']}")

print()
print('#6.8')
print()

rat = {'owner': 'Jenny', 'age': 2, 'price': 200}
cat = {'owner': 'Olivia', 'age': 12, 'price': 600}
dog = {'owner': 'Emma', 'age': 1.5, 'price': 1200}

animals = [rat, cat, dog]

for a in animals:
	print(f"\nOwner: {a['owner']}")
	print(f"Age: {a['age']}")
	print(f"Price: {a['price']}")

print()
print('#6.9')
print()	


favorite_places = {'Alice': ['Paris', 'London', 'Prague'], 'Mia': ['Kiev', 'Moscow', 'Rome'],
'Peter': ['Kiev', 'Berlin', 'Athens'] }

for name, places in favorite_places.items():
	print(f"\n{name}'s favorite places are: ")
	for place in places:
		print(f"\t{place}") 