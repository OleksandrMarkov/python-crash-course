from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
	# головна
    path('', views.index, name = 'index'),

    #усі теми
    path('topics/', views.topics, name = 'topics'),

    #тема
	path('topics/<int:topic_id>/', views.topic, name = 'topic'),

	#додати нову тему
	path('new_topic/', views.new_topic, name = 'new_topic'),

	#додати новий допис
	path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),

	#редагувати допис
	path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),    
]
