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

print()

# 4.10
# slices for arr 5
tmp1 = arr5[:3]
tmp2 = arr5[3:6]
tmp3 = arr5[-3:]


for a in tmp1:
	print(str(a) + " ", end = "")

print()

for a in tmp2:
	print(str(a) + " ", end = "")

print()

for a in tmp3:
	print(str(a) + " ", end = "")		

# 4.11
friend_pizzas = pizza_lst[:]

pizza_lst.append('new_p')
friend_pizzas.append('new_p2')

print('My favorite pizzas are:')
print(pizza_lst)

print()

print("My friend's favorite pizzas are:")
print(friend_pizzas)


#4.12

for f in friend_pizzas:
	print(f)

print()

# 4.13

foods = ('borshch', 'tea', 'coffee', 'cake', 'porridge')

for f in foods:
	print(f + ' |', end = "")	

print()

foods = ('borshch', 'good tea', 'coffee', 'tasty cake', 'porridge')

for f in foods:
	print(f + ' |', end = "")

# 4.14, 4.15 -> pep8		