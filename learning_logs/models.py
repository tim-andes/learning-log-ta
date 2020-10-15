from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	"""A topic the user is learning about.

	Attributes:
		text: CharField instance.
		date_added: DateTimeField instance.
		owner: ForeignKey of User instance.

	Method: __str__
	"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Something specific learned about a topic.

	Attributes:
		topic: ForeignKey of Topic instance.
		text: TextField instance.
		date_added: DateTimeField instance.

	Class: Meta, for proper pluralization in admin page.

	Method: __str__
	"""

	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return f"{self.text}"