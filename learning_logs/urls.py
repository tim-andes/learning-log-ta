"""Defines URL patterns for learning_logs.""" # 1
from django.urls import path # 2
from . import views # 3

app_name = 'learning_logs' # 4

urlpatterns = [ # 5
	# Home/Index page: http://localhost:8000/
	path('', views.index, name='index'), # 6
	# Topics page: http://localhost:8000/topics/
	path('topics/', views.topics, name='topics'), # 7
	# Detail page for single topic: http://localhost:8000/topics/1/
	path('topics/<int:topic_id>/', views.topic, name='topic'), # 8
	# Page for adding a new topic:
	path('new_topic/', views.new_topic, name='new_topic'), # 9
	# Page for adding a new entry:
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # 10
	# Page for editing an entry:
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), # 11
]

# 1. To make it clear which urls.py we’re working in, we add a docstring at the
# beginning of the file
#
# 2. We then import the path function, which is needed when mapping URLs
# to views.
#
# 3. We also import the views module
# The dot tells Python to import the views.py module from the same directory
# as the current urls.py module
#
# 4. The variable app_name helps Django distinguish
# this urls.py file from files of the same name in other apps within the
# project
#
# 5. The variable urlpatterns in this module is a list of individual pages
# that can be requested from the learning_logs app.
#
# 6. Specifies which function to call
# in views.py. When a requested URL matches the pattern we’re defining,
# Django calls the index() function from views.py (we’ll write this view func-
# tion in the next section). The third argument provides the name index for
# this URL pattern so we can refer to it in other code sections. Whenever we
# want to provide a link to the home page, we’ll use this name instead of writ-
# ing out a URL.
#
# 7. We’ve simply added topics/ into the string argument used for the
# home page URL. When Django examines a requested URL, this pat-
# tern will match any URL that has the base URL followed by topics. You can
# include or omit a forward slash at the end, but there can’t be anything
# else after the word topics, or the pattern won’t match. Any request with a
# URL that matches this pattern will then be passed to the function topics()
# in views.py.
#
# 8. Let’s examine the string 'topics/<int:topic_id>/' in this URL pattern.
# The first part of the string tells Django to look for URLs that have the word
# topics after the base URL. The second part of the string, /<int:topic_id>/ ,
# matches an integer between two forward slashes and stores the integer
# value in an argument called topic_id .
# When Django finds a URL that matches this pattern, it calls the view
# function topic() with the value stored in topic_id as an argument. We’ll use
# the value of topic_id to get the correct topic inside the function.

# 9. This adds a link for new_topic. Will enable users to add new topics.
# Next, we need to add new_topic() to views.py

# 10. This URL pattern matches any URL with the form http://localhost:
# 8000/new_entry/id/ , where id is a number matching the topic ID. The code
# <int:topic_id> captures a numerical value and assigns it to the variable
# topic_id . When a URL matching this pattern is requested, Django sends
# the request and the topic’s ID to the new_entry() view function.

# 11. The ID passed in the URL (for example, http://localhost:8000/edit
# _entry/1/) is stored in the parameter entry_id . The URL pattern sends
# requests that match this format to the view function edit_entry() .

