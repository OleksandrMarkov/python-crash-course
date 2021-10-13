print('# introduction')
print()

d1 = {'color': 'green', 'points': 5,}

print(d1)
print()

d1['x'] = 0
d1['y'] = 20

print(d1)
print()

del d1['x']

print(d1)
print()

# instead of d1[price] if you do not sure that 'price' key exists
price = d1.get('price', 'This dictionary has no key "price"!')
print(price)

print('#6.1')
print()

friend = {'first_name' : 'Max', 'last_name' : 'Kennedy', 'age': 30, 'city': 'Virginia'}
print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])

print('#6.2')
print()

favorite_numbers = {'Jack': 100, 'Alex': 1, 'Tom': 23, 'Alice': 2, 'Ann':60}
print(favorite_numbers['Jack'])
print(favorite_numbers['Alex'])
print(favorite_numbers['Tom'])
print(favorite_numbers['Alice'])
print(favorite_numbers['Ann'])

# 6.3 is boring ;)