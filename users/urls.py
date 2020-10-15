"""Defines URL patters for users."""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	# Include default auth urls
	path('', include('django.contrib.auth.urls')),
	# Register
	path('register/', views.register, name='register'),
]