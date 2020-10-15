from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
	"""The home page for Learning Log.

	Args:
		request (obj)

	Returns:
		render:
			request
			learning_logs/index.html
	"""
	return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
	"""List all topics in order.

	Args:
		request (obj)

	Attributes:
		topics: User created topics ordered chronologically.
		context: A means to reference {{ topics }} in .html files.

	Returns:
		render:
			request
			learning_logs/topics.html
			context
	"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
	"""Displays a single topic and all its entries from newest to oldest.

	Args:
		request (obj)
		topic_id: value captured by the expression /<int:topic_id>/
			as seen in learning_logs/urls.py

	Attributes:
		topic: User created topic. If non-owner attempts to visit url 404
			will be raised.
		entries: Entries from newest to oldest.
		context: A means to reference {{ entries }}, {{ topic }} in .html
			files.

	Returns:
		render:
			request
			learning_logs/topic.html
			context
	"""
	topic = get_object_or_404(Topic, id=topic_id)

	# Check that topic belongs to the current user
	check_topic_owner(topic.owner, request.user)

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
	"""When User adds a new topic.

	Args:
		request (obj)

	Attributes:
		form: TopicForm instance, either blank or filled out.
		new_topic: A new topic; form. Form data saved after User check.
		context: A means to reference {{ form }} in .html files.

	Returns:
		redirect:
			Back to user's topics page.
		render:
			request
			learning_logs/new_topic.html
			context
	"""
	if request.method != 'POST':
		# No data submitted yet; provide a blank form
		form = TopicForm()
	else:
		# POST data submitted; process data
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	"""Add a new entry for selected topic.

	Args:
		request (obj)
		topic_id: value captured by the expression /<int:topic_id>/
			as seen in learning_logs/urls.py

	Attributes:
		topic: User created topic by id.
		form: EntryForm instance, either blank or filled out.
		new_entry: A new entry; form. Form data saved after User check.
		context: A means to reference {{ topic }}, {{ form }} in .html files.

	Returns:
		redirect:
			Back to particular topic via id.
		render:
			request
			learning_logs/new_entry.html
			context
	"""
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST':
		form = EntryForm()
	else:
		# POST data submitted; process data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)

	# Display a blank or invalid form
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry.

	Args:
		request (obj)
		entry_id: value captured by the expression /<int:entry_id>/
			as seen in learning_logs/urls.py

	Attributes:
		entry: User created entry by id.
		topic: ForeignKey of Topic instance. See models.py.
		form: EntryForm instance, either blank or filled out.
		context: A means to reference {{ entry }}, {{ topic }}, {{ form }} in
			.html files.

	Returns:
		redirect:
			Back to particular topic via id.
		render:
			request
			learning_logs/new_entry.html
			context
	"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(owner, request):
	"""Verify that user owns topic they're attempting to view.

	Args:
		owner: ForeignKey of User instance. See models.py.
		request (obj)

	Raises:
		404: If owner is not the one making the request.
	"""
	if owner != request:
		raise Http404