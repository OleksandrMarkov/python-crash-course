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

		for i in range(4):
			ch = choice(all_ch)
			self.ticket.append(ch)
			all_ch.remove(ch)	

	def show(self):
		if self.ticket:
			#print(i, end = "")
			#print(str(self.ticket))
			self.ticket = ''.join(map(str, self.ticket)).title()
			print(f'The ticket "{self.ticket}" has won the prize!')	