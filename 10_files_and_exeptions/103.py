filename = 'guest.txt'

your_name = input("Name: ")

with open(filename, "w") as file_object:
	file_object.write(your_name)