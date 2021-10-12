#5.1
car = 'audi'
food = 'cake'
id = 25
result = 200
music = 'rock'

print('Is car == "BMW"? I predict FALSE')
print(car == "BMW")
print()
print('Is car == "audi"? I predict TRUE')
print(car == "audi")
print()
print('Is food == "vegetables"? I predict FALSE')
print(car == "vegetables")
print()
print('Is food == "cake"? I predict TRUE')
print(food == "cake")
print()
print('Is id == "34"? I predict FALSE')
print(id == "34")
print()
print('Is id == "25"? I predict TRUE')
print(id == 25)
print()
print('Is result == "200"? I predict FALSE')
print(result == "200")
print()
print('Is result == 200? I predict TRUE')
print(result == 200)
print()
print('Is music == "jazz"? I predict FALSE')
print(music == "jazz")
print()
print('Is music == "rock"? I predict TRUE')
print(result == 'rock')

print()
print('#5.2')
#5.2
print('Cake' == food)
print('sweet' != food)

print(f'id = {id}, id < 22 ? {id < 22}')
print(f'id = {id}, id >= 23 ? {id >= 23}')
print(f'id = {id}, id <= 40 ? {id <= 40}')
print(f'id = {id}, id > 25 ? {id > 25}')

print(f"Is car = {car.title()} ? {car.title() == 'Audi'}")

machine = 'Washer'

print(f"Is {machine.lower()} a washer? {machine.lower() == 'washer'}")
print(f"Is id == 100 and result == {result} ?  {id == 100 and result == result}")

lst = [25, 45, 32, 'test', 'test2', 12]
print(f"Is 25 in lst? {25 in lst}")
print(f"Is 25 in lst? {25 in lst}")

print()
print('# 5.3')

alien_color = 'red'
score = 0

if alien_color == 'red':
	score += 5
	print(f"Score is {score}.")

if score == 5:
	print(f'Score is {score}.')
else:
	pass	

print()
print('# 5.4')

alien_color = 'yellow'

if alien_color == 'green':
	print('You get 5 points for killing an alien.')
else:
	score += 10
	print('You get 10 points.')

if alien_color == 'yellow':
	print('Alien is yellow')
else:
	print("Alien's color is unknown.")

print()

print()
print('# 5.5')

if alien_color == 'green':
	score += 5
	print('You get 5 points.')
elif alien_color == 'yellow':
	score += 10
	print('You get 10 points.')	
elif alien_color == 'red':
	score += 15
	print('You get 15 points.')	

print()
print('# 5.6')

age = 65

if age < 2:
	print("It's a suckling")
elif age < 4: 
	print("It's a baby")
elif age < 13:
	print("It's a child")
elif age < 20:
	print("It's a teenager")
elif age < 65:
	print("It's an adult")
else:
	print("It's an aged")			

print()
print('# 5.7')

favorite_fruits = ['apples', 'pears', 'plums', 'oranges', 'grape', 'lemons']

if 'bananas' in favorite_fruits:
	print('You really like bananas!')

if 'apples' in favorite_fruits:
	print('You really like apples!')

if 'oranges' in favorite_fruits:
	print('You really like oranges!')

if 'pomegranates' in favorite_fruits:
	print('You really like pomegranates!')

if 'tomatoes' in favorite_fruits:
	print('You really like tomatoes!')

# lst = [...]
# if lst : 
#	...
#	if lst is not empty

print()
print('# 5.8, 5.9')

lst = ['Jack', 'admin', 'Tom', 'Bobby', 'Helen']

if lst:
	for person in lst:
		if person == 'admin':
			print(f'Hello {person}, would you like to see a status report?')
		else:
			print(f'Hello {person}, thank you for logging in again')	
else:
	print('We need to find some users')

print()
print('# 5.10')

# checking login uniqueness
current_users = ['Nick', 'Jack', 'Andy', 'Alice', 'Kate']
current_users_lower = [c.lower() for c in current_users]

for c in current_users_lower:
	print(c)	

print()

new_users = ['jack', 'Ann', 'KatE', 'Tony', 'Mike']

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f'Nickname "{new_user}" is taken. You should  chose other nickname')
	else:
		print(f'Your nickname "{new_user}" is not taken')	

# 5.11 is done

# 5.12 calculator, website, game, recommendation system