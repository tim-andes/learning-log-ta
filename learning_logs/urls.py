"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
	# Home/Index page
	path('', views.index, name='index'),
	# Topics
	path('topics/', views.topics, name='topics'),
	# Topic
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# New Topic
	path('new_topic/', views.new_topic, name='new_topic'),
	# New Entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Edit Entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]