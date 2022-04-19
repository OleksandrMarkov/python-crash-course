while True:
	print("Press q for quit")
	try:
		first_num = input("First number: ")
		if first_num == 'q':
			break
		first_num = int(first_num)
		second_num = input("Second number: ")
		if second_num == 'q':
			break
		second_num = int(second_num)
	except ValueError:
		print("You can't add non-numeric values!")
	else:
		sum = first_num + second_num
		print(f"The sum is {sum}.")	