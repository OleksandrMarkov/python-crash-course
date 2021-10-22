from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . models import Topic, Entry
from . forms import TopicForm, EntryForm

def check_topic_owner(topic, request):
	return topic.owner == request.user

"""Головна"""
def index(request):
	return render(request, 'learning_logs/index.html')

@login_required # якщо користувач автентифікований
def topics(request):
	"""Впорядковані теми """
	topics = Topic.objects.filter(owner = request.user).order_by('date_added')
	context = {'topics' : topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id = topic_id)
	if check_topic_owner(topic, request) == False:
		raise Http404		
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic' : topic, 'entries' : entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""Нова тема"""
	if request.method != 'POST':
		# Даних не відправлено; створити порожню форму
		form = TopicForm()
	else:
		# обробити дані
		form = TopicForm(data = request.POST)
		if form.is_valid(): # якщо форма коректно заповнена
			new_topic = form.save(commit = False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics') # переадресація на сторінку topics

	#показати порожню/недійсну форму
	context = {'form' : form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id = topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data = request.POST)
		if form.is_valid():
			if check_topic_owner(topic, request) == False:
				raise Http404 
			else:	
				new_entry = form.save(commit = False) # поки атрибут 'topic' не вказано, збереження
				# в БД не відбувається
				new_entry.topic = topic
				new_entry.save()
				# у всіх дописах з цією темою з'явиться новий допис
				return redirect('learning_logs:topic', topic_id = topic_id)
	
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic
	if check_topic_owner(topic, request) == False:
		raise Http404

	if request.method != 'POST':
		# django створює попередньо заповнену форму
		form = EntryForm(instance = entry)
		#і тепер можна редагувати
	else:
		# форма з урахуванням оновлень
		form = EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			# повертаємось до теми з оновленою версією допису
			return redirect('learning_logs:topic', topic_id = topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)