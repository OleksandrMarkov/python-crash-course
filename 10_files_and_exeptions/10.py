with open ('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)

# Does your birthday appear in the first million digits of pi?
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()	
pi_string = ''
for line in lines:
	pi_string += line.strip()
#birthday = input()
birthday = '061099' 
if birthday in pi_string:
	print('YES')
else:
	print('NO')	

