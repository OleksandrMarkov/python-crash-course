from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model): # ТЕМА
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User, on_delete = models.CASCADE)
	def __str__(self):
		return self.text

class Entry(models.Model): #ДОПИС
	""" 1 тема <---> багато дописів """
	# при каскадному видаленні разом з темою видаляються і дописи по ній 
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE) 

	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'
	def __str__(self):
		"""Якщо тема більше 50 символів, відображаємо 50 символів і три крапки"""
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
			