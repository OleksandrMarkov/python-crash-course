from random import *

class Lottery:
	lst = []
	ticket = []

	def __init__(self):
		for i in range(10):
			self.lst.append(randint(0,9))
		for i in range(5):
			self.lst.append(chr(randrange(97,97 + 26)))	
	
	def make_a_ticket(self):
		all_ch = self.lst[:] 
		self.ticket = []

		for i in range(4):
			ch = choice(all_ch)
			self.ticket.append(ch)
			all_ch.remove(ch)

	def return_ticket(self):
		if self.ticket:
			self.ticket = ''.join(map(str, self.ticket)).upper()
			return self.ticket
		return None				

	def show(self):
			print(f'The ticket "{self.return_ticket()}" has won the prize!')	