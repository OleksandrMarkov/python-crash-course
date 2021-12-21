filename = 'lorem.txt'

# read all
with open(filename) as file_object:
	contents = file_object.read()
print(contents)

# read lines in cycle
with open(filename) as file_object:
	for line in file_object:
			print(line)

#read lines to list
with open(filename) as file_object:
	lines = file_object.readlines()
lst = []
for line in lines:
	lst.append(line)
for l in lst:
	print(l)	
