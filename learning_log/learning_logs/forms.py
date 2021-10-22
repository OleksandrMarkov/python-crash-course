from django import forms

from . models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':''} # не продукувати написи

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		# ширина віджету "Текстове поле" - 80 стовпців замість 40
		widgets = {'text': forms.Textarea(attrs = {'cols' : 80})}