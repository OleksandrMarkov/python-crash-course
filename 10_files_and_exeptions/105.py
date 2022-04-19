filename = "answers.txt"
beginning = "I like programming, because "

while True:
	print("Why do you like programming? Press q for quit")
	answer = input(beginning)
	if answer == 'q':
		break
	with open(filename, 'a') as f:
		f.write(beginning + answer + '\n')

