filename = 'lorem.txt'

# read lines in cycle
lst = []

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line.replace('diam', 'vjfjlfgjflgjfdlkgj')
	print(line)

	