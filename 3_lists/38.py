#3.8

places = ['paris', 'vienna', 'london', 'kiev', 'prague']

print(sorted(places) == places) #3.8.1

print(places) #3.8.2
print(sorted(places)) #3.8.3
print(places) #3.8.4

# 3.8.5
temp = sorted(places) 
temp.reverse()
print(temp)

print(places) #3.8.6


places.reverse() # 3.8.7
print(places)

places.reverse() # 3.8.8
print(places)

places.sort() # 3.8.9
print(places)

places.sort(reverse = True) # 3.8.10
print(places)

# 3.9-3.11 is not interesting ;)