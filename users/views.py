from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
	"""Register a new user."""
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

"""
We import the render() and redirect() functions. Then we import the
login() function to log the user in if their registration information is cor-
rect. We also import the default UserCreationForm . In the register() function,
we check whether or not we’re responding to a POST request. If we’re not, we
make an instance of UserCreationForm with no initial data [9].

If we’re responding to a POST request, we make an instance of
UserCreationForm based on the submitted data [12]. We check that the data
is valid [14]—in this case, that the username has the appropriate characters,
the passwords match, and the user isn’t trying to do anything malicious
in their submission.

If the submitted data is valid, we call the form’s save() method to save
the username and the hash of the password to the database [15]. The save()
method returns the newly created user object, which we assign to new_user .
When the user’s information is saved, we log them in by calling the login()
function with the request and new_user objects [17], which creates a valid ses-
sion for the new user. Finally, we redirect the user to the home page [18],
where a personalized greeting in the header tells them their registration
was successful.
At the end of the function we render the page, which will either be a
blank form or a submitted form that is invalid.
"""
