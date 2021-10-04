# 4.1

pizza_lst = ['p1', 'p2', 'p3']

for p in pizza_lst:
	print(p)

for p in pizza_lst:
	print(f"I like {p} pizza")
print("I really love pizza!")

# 4.2

animals	= ['dog', 'horse', 'pig']

for a in animals:
	print(f"The {a}s are useful for humanity")
print("Any of them are useful for humanity")


# 4.3

# 4.31
for i in range(1,21):
	print(i)
# 4.32
arr = [i for i in range(1,21)]
print(arr)

#print(i for i in range(1,21))

# 4.4, 4.5
arr2 = [i for i in range(1, 1_000_001)]
print(min(arr2))
print(max(arr2))
print(sum(arr2))

#4.6
arr3 = [i for i in range(1,21,2)]
for a in arr3:
	print(str(a) + " ", end = "")

print()

#4.7
arr4 = [i for i in range(3,31,3)]
for a in arr4:
	print(str(a) + " ", end = "")

print()

#4.8, 4,9
arr5 = [i**3 for i in range(1,11)]
for a in arr5:
	print(str(a) + " ", end = "")