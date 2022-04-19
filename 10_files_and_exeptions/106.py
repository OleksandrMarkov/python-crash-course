try:
	first_num = input("First number: ")
	first_num = int(first_num)
	second_num = input("Second number: ")
	second_num = int(second_num)
except ValueError:
	print("You can't add non-numeric values!")
else:
	sum = first_num + second_num
	print(f"The sum is {sum}.")	