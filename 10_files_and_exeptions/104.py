import time
filename = 'guest_book.txt'

while True:
	print("Your name? Q for quit")
	name = input("My name is ")
	if name == 'Q':
		break
	print("Hello, " + name + "!")	

	t = time.localtime()
	time_val = time.strftime("%m/%d/%Y, %H:%M", t)

	with open(filename, 'a') as f:
		f.write(f"Our new guest {name} visited us at {time_val}.\n")