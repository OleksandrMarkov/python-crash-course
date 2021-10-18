from lottery import Lottery

l = Lottery()
#l.make_a_ticket()
#l.show()

my_ticket = '2S3K'
ticket = ''
attempts = 0

while ticket != my_ticket:
	ticket = l.make_a_ticket()
	print(l.return_ticket())
	attempts +=1
	print(attempts)
	if attempts > 2_000_000:
		exit(0)

print(f"My ticket: {my_ticket}")
print(f"Iterations: {attempts}")