from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
	# URL автентифікації за замовчуванням
	path('', include('django.contrib.auth.urls')),
	path('register/', views.register, name = 'register'),
]