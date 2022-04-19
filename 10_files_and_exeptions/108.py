cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

def get_names(filename):
	try:
		with open (filename) as f:
			names = f.readlines()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} doesn't exist.")
	else:
		return names			

cats_names = get_names(cats_file)
dogs_names = get_names(dogs_file)

if cats_names:
	print('Cats names:')
	for c in cats_names:
		print(c, end = '')
	print()
if dogs_names:	
	print('Dogs names:')
	for d in dogs_names:
		print(d, end = '')