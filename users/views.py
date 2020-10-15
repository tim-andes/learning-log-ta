from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Register a new user.

	Args:
		request (obj)

	Attributes:
		form: UserCreationForm instance, either blank or filled out.
		new_user: A new user; form. Form data saved after User check.
		context: A means to reference {{ form }} in .html files.

	Returns:
		redirect:
			Back to home page.
		render:
			request
			registration/register.html
			context
	"""
	if request.method != 'POST':
		# Display blank registration form
		form = UserCreationForm()
	else:
		# Process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the new user in then redirect to home page
			login(request, new_user)
			return redirect('learning_logs:index')

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'registration/register.html', context)