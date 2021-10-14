# introduction

print('# introduction')

#msg = input("tell me sth: ")
#print(msg)

print()
print('#7.1')

#msg = input("What auto would you like to rent? ")
#print(f"I will try to find {msg} for you.")

print()
print('#7.2')

#tables = input("How many tables would you like to book? ")
#tables = int(tables)

#if tables > 8:
#	print("You will have to wait")
#else:
#	print("Your tables are ready")

print()
print('#7.3')

#num = input("Number: ")
#num = int(num)

#if num % 10 == 0:
#	print(f"{num} is multiple to ten.")
#else:
#	print(f"{num} is not multiple to ten.")


print()
print('#7.4')

#ingredient = ""
#while ingredient != 'quit':
#	ingredient = input("Ingredient (enter 'quit' when you are finished): ")
#	if ingredient != 'quit':
#		print(f"{ingredient} added to our pizza!")


print()
print('#7.5')

#while True:
#	age = input("How old are you? ")
#	age = int(age)

#	if age < 3:
#		print(age)
#		print("The entrance is free")
#	elif 3 <= age <= 12:
#		ticket_price = 10
#		print(age) 
#		print(f"The ticket costs {ticket_price}$.")
#	else:
#		ticket_price = 15
#		print(age) 
#		print(f"The ticket costs {ticket_price}$.")	
#	break

print('#7.6')
print()

#active = True
#ingredient = ""
#while active:
#	ingredient = input("Ingredient (enter 'quit' when you are finished): ")
#	if ingredient == 'quit':
#		break
#	else:
#		print(f"{ingredient} added to our pizza!")


print('#7.7')
print('eternal cycle')
#x = 0
#while x < 1:
#	print(x)

#removing all cats using cycle

#pets = ['cat', 'dog', 'swine', 'dog', 'cat', 'rabbit', 'rabbit', 'cat', 'mouse']

#while 'cat' in pets:
#	pets.remove('cat')
#print(pets)

print()
print('#7.8')
sandwich_orders = ['s1', 's2', 's3', 's4', 's5']
finished_sandwiches = []

#while sandwich_orders:
#	tmp_order = sandwich_orders.pop()
#	print(f"I made you {tmp_order} sandwich!")
#	finished_sandwiches.append(tmp_order)
#print("Sandwiches are ready:")
#for fs in finished_sandwiches:
#	print(f"\t{fs}")

print()
print('#7.9')
sandwich_orders = ['s1', 'pastrami', 's2', 'pastrami', 's3', 'pastrami', 
's4', 'pastrami', 'pastrami', 's5', 'pastrami']
print('We are out of pastrami')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	tmp_order = sandwich_orders.pop()
	print(f"I made you {tmp_order} sandwich!")
	finished_sandwiches.append(tmp_order)

print("Sandwiches are ready:")
for fs in finished_sandwiches:
	print(f"\t{fs}")	


print()
print('#7.10')

polling_active = True
responses = {}

while polling_active:
	name = input("\nWhat is your name? ")
	place = input("\nWhere would you like to visit? ")
	responses[name] = place

	repeat = input('\nWould you like to let another person respond? (yes/no) ')

	if repeat == 'no':
		polling_active = False

print("\n --- Poll results ---")

for name, place in responses.items():
	print(f"{name} would like to visit {place}")
