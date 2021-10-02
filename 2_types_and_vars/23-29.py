# 2.3

name = 'X'
greeting = f"Hello, {name}, would you like to learn some Python today?"
print(greeting)

# 2.4

name = 'some one'
print(name.title())

#2.5

#print('Федір Достоєвський якось сказав: "Без великодушних ідей людство жити не може".')

#2.6

text = 'Федір Достоєвський якось сказав:'
quotation = 'Без великодушних ідей людство жити не може'

phrase1 = '{} "{}".'.format(text, quotation)
phrase2 = f'{text} "{quotation}".'

print(phrase1)
print(phrase2)
print(phrase2 == phrase1)

#2.7

text = '\n\ttext.\n'
print(text)
print(text.strip())

#2.8
print(5+3)
print(10-2)
print(1*8)
print(int(40/5))

#2.9
number = 10

print(f"My favorite number is {number}.")