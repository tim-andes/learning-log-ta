"""Defines URL patters for users."""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	# Include default auth urls
	path('', include('django.contrib.auth.urls')),
	# Registration page
	path('register/', views.register, name='register'),
]

"""
[line 3] We import the path function, and then import the include function so
we can include some default authentication URLs that Django has defined.
These default URLs include named URL patterns, such as 'login' and
'logout' . We set the variable app_name to 'users' so Django can distinguish
these URLs from URLs belonging to other apps [line 5]. Even default URLs pro-
vided by Django, when included in the users app’s urls.py file, will be acces-
sible through the users namespace.

The login page’s pattern matches the URL http://localhost:8000/users
/login/ [line 9]. When Django reads this URL, the word users tells Django to look in
users/urls.py, and login tells it to send requests to Django’s default login view.
"""