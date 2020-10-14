from django.shortcuts import render, redirect, get_object_or_404 # 1
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry # 3
from .forms import TopicForm, EntryForm

# 'redirect' above and line 3 added for new_topic()

# Create your views here.
def index(request): # 2
	"""The home page for Learning Log."""
	return render(request, 'learning_logs/index.html')


@login_required
def topics(request): # 4
	"""Show all topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added') # 5
	context = {'topics': topics} # 6
	return render(request, 'learning_logs/topics.html', context) # 7

@login_required
def topic(request, topic_id): # 8a
	"""Shows a single topic and all its entries."""
	topic = get_object_or_404(Topic, id=topic_id) # b

	# Make sure the topic belows to the current user
	check_topic_owner(topic.owner, request.user)

	entries = topic.entry_set.order_by('-date_added') # c
	context = {'topic': topic, 'entries': entries} # d
	return render(request, 'learning_logs/topic.html', context) # e

@login_required
def new_topic(request): # 9.
	"""User add new topic."""
	if request.method != 'POST': # a
		# No data submitted; create a blank form; GET request
		form = TopicForm() # b
	else:
		# POST data submitted; process data.
		form = TopicForm(data=request.POST) # c
		if form.is_valid(): # d
			# form.save() # e - Removed when we gave Topic ownership to users
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics') # f

	# Display a blank or invalid form
	context = {'form': form} # g
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id): # 10
	"""Add a new entry for selected topic."""
	topic = Topic.objects.get(id=topic_id) # a
	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST': # b
		# No data submitted; create a blank form.
		form = EntryForm() # c
	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST) # d
		if form.is_valid():
			new_entry = form.save(commit=False) # e
			new_entry.topic = topic # f
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id) # g

	# Display a blank or invalid form
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id): # 11
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id) # a
	topic = entry.topic
	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry) # b
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST) # c
		if form.is_valid():
			form.save() # d
			return redirect('learning_logs:topic', topic_id=topic.id) # e

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(owner, request):
	"""Verify that user owns topic they're attempting to view."""
	if owner != request:
		raise Http404

## 1.
## Currently, this file just imports the render() function, which renders
## the request based on the data provided by views.

## 2.
## When a URL request matches the pattern we just defined, Django looks
## for a function called index() in the views.py file. Django then passes the
## request object to this view function. In this case, we don’t need to process
## any data for the page, so the only code in the function is a call to render() .
## The render() function here passes two arguments—the original request
## object and a template it can use to build the page. Let’s write this template.

## 3. First, import model associated with the data we need.

## 4. The topics() function needs one parameter: the request object Django received
## from the server

## 5. We query the database by asking for the Topic objects, sorted by the
## date_added attribute. We store the resulting queryset in topics.
# filter(owner=request.user) -- When a user is logged in, the request object has a request.user attri-
# bute set that stores information about the user. The query Topic.objects
# .filter(owner=request.user) tells Django to retrieve only the Topic objects
# from the database whose owner attribute matches the current user.

## 6. We define a context that we’ll send to the template. A context is a
## dictionary in which the keys are names we’ll use in the template to access
## the data, and the values are the data we need to send to the template. In this
## case, there’s one key-value pair, which contains the set of topics we’ll display
## on the page.

## 7. When building a page that uses data, we pass the context vari-
## able to render() as well as the request object and the path to the template

## 8. This is the first view function that requires a parameter other than the
# request object. The function accepts the value captured by the expression
# (id)and stores it in topic_id [a]. At [b] we use get() to retrieve the
# topic, just as we did in the Django shell. [UPDATE] this was changed per p.460
# At [c] we get the entries associated
# with this topic, and we order them according to date_added. The minus sign
# in front of date_added sorts the results in reverse order, which will display the
# most recent entries first. We store the topic and entries in the context dic-
# tionary [d] and send context to the template topic.html [e]. On [d]: A context is a
# dictionary in which the keys are names we’ll use in the template to access
# the data, and the values are the data we need to send to the template.

## NOTE, #8: The code phrases at [b] and [c] are called queries, because they query the database for
# specific information. When you’re writing queries like these in your own projects, it’s
# helpful to try them out in the Django shell first. You’ll get much quicker feedback in
# the shell than you will by writing a view and template, and then checking the results
# in a browser.

## 9.
"""
The new_topic() function takes in the request object as a parameter.
When the user initially requests this page, their browser will send a GET
request. Once the user has filled out and submitted the form, their browser
will submit a POST request. Depending on the request, we’ll know whether
the user is requesting a blank form (a GET request) or asking us to process
a completed form (a POST request).

The test at [a] determines whether the request method is GET or POST.
If the request method isn’t POST, the request is probably GET, so we need
to return a blank form (if it’s another kind of request, it’s still safe to return
a blank form). We make an instance of TopicForm [b], assign it to the variable
form , and send the form to the template in the context dictionary [g]. Because
we included no arguments when instantiating TopicForm , Django creates a
blank form that the user can fill out.

If the request method is POST, the else block runs and processes the
data submitted in the form. We make an instance of TopicForm [c] and pass
it the data entered by the user, stored in request.POST. The form object that’s
returned contains the information submitted by the user.

We can’t save the submitted information in the database until we’ve
checked that it’s valid [d]. The is_valid() method checks that all required fields
have been filled in (all fields in a form are required by default) and that the
data entered matches the field types expected—for example, that the length
of text is less than 200 characters, as we specified in models.py in Chapter 18.
This automatic validation saves us a lot of work. If everything is valid, we can
call save() [e], which writes the data from the form to the database.

Once we’ve saved the data, we can leave this page. We use redirect() to
redirect the user’s browser to the topics page, where the user should see the
topic they just entered in the list of topics.

The context variable is defined at the end of the view function, and the
page is rendered using the template new_topic.html, which we’ll create next.
This code is placed outside of any if block; it will run if a blank form was
created, and it will run if a submitted form is determined to be invalid. An
invalid form will include some default error messages to help the user sub-
mit acceptable data.
"""


## 10.
"""
We update the import statement to include the EntryForm we just made.
The definition of new_entry() has a topic_id parameter to store the value it
receives from the URL. We’ll need the topic to render the page and process
the form’s data, so we use topic_id to get the correct topic object at [a].
At [b] we check whether the request method is POST or GET. The
if block executes if it’s a GET request, and we create a blank instance of
EntryForm [c].

If the request method is POST, we process the data by making an
instance of EntryForm , populated with the POST data from the request
object [d]. We then check whether the form is valid. If it is, we need to set
the entry object’s topic attribute before saving it to the database. When we
call save() , we include the argument commit=False [e] to tell Django to create
a new entry object and assign it to new_entry without saving it to the data-
base yet. We set the topic attribute of new_entry to the topic we pulled from
the database at the beginning of the function [f]. Then we call save() with
no arguments, saving the entry to the database with the correct associated
topic.

The redirect() call at { requires two arguments—the name of the view
we want to redirect to and the argument that view function requires. Here,
we’re redirecting to topic() , which needs the argument topic_id . This view
then renders the topic page that the user made an entry for, and they should
see their new entry in the list of entries.

At the end of the function, we create a context dictionary and render the
page using the new_entry.html template. This code will exe
"""
## 11.
"""
We first import the Entry model. At [a] we get the entry object that the
user wants to edit and the topic associated with this entry. In the if block,
which runs for a GET request, we make an instance of EntryForm with the
argument instance=entry [b]. This argument tells Django to create the form
prefilled with information from the existing entry object. The user will see
their existing data and be able to edit that data.

When processing a POST request, we pass the instance=entry argument
and the data=request.POST argument [c]. These arguments tell Django to cre-
ate a form instance based on the information associated with the existing
entry object, updated with any relevant data from request.POST . We then
check whether the form is valid; if it is, we call save() with no arguments
because the entry is already associated with the correct topic [d]. We then
redirect to the topic page, where the user should see the updated version
of the entry they edited [e].

If we’re showing an initial form for editing the entry or if the submitted
form is invalid, we create the context dictionary and render the page using
the edit_entry.html template.
"""

"""
[13] We first import the login_required() function. We apply login_required()
as a decorator to the topics() view function by prepending login_required with
the @ symbol. As a result, Python knows to run the code in login_required()
before the code in topics() .

The code in login_required() checks whether a user is logged in, and
Django runs the code in topics() only if they are. If the user isn’t logged in,
they’re redirected to the login page.

To make this redirect work, we need to modify settings.py so Django
knows where to find the login page. Add the following at the very end of
settings.py
"""

"""
[line 46-48]
When we first call form.save() , we pass the commit=False argument because
we need to modify the new topic before saving it to the database [46]. We then
set the new topic’s owner attribute to the current user [47]. Finally, we call save()
on the topic instance just defined [48]. Now the topic has all the required data
and will save successfully
"""