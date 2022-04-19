files = ['chapter1.txt', 'chapter2.txt']
count = 0
for file in files:
	try:
		with open (file, encoding = 'utf-8') as f:
			text = f.read()
	except FileNotFoundError:
		print(f"The file {file} doesn't exist.")	
	else:
		the = text.count('the ') + text.count('The ')
		count += the

if count:
	print(f"The count of 'the' in files is {count}.")				