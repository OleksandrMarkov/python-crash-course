# 3.1, 3.2

friends = ['James', 'Max', 'Steve', 'John']

for f in friends:
	#print(f)
	print(f"Hello, {f}!")


# 3.3

cars = ['Honda', 'Tavria', 'Lada', 'Peugeaut']

print(f"I would like to own a {cars[0]} motorcycle")

#3.4

guests = ['x', 'y', 'z']
for g in guests:
	print(f"{g}! Welcome!")

#3.5.1, 3.5.2
print(guests.pop(1)) # 'y' will not come
guests.insert(1, 'Q')
print(guests)

#3.5.3	
for g in guests:
	print(f"{g}! Welcome!")

#3.6
for g in guests:
	print(f"{g}, I have found the bigger table")

guests.insert(0, 'new1')
guests.insert(2, 'new2')	
guests.append('new3')

for g in guests:
	print(f"{g}! Welcome!")

#3.7
print("I'm sorry, I can only invite two friends")

while(len(guests) > 2):
	no_invited = guests.pop()
	print(f"{no_invited.title()}, I cannot invite you.")

print()
print(f"{guests[0]}, you are still invited")
print(f"{guests[1]}, you are still invited")

del guests[1]
del guests[0]

print('guests:')
print(guests)	