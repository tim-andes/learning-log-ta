from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""A topic the user is learning about.
	Two attributes: text, date_added
	One method: __str__
	"""
	text = models.CharField(max_length=200) # 1.
	date_added = models.DateTimeField(auto_now_add=True) # 2.
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self): # 3.
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model): # 1.
	"""Something specific learned about a topic."""

	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # 2.
	text = models.TextField() # 3.
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta: # 4.
		verbose_name_plural = 'entries'

	def __str__(self): # 5.
		"""Return a string representation of the model."""
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return f"{self.text}"

# [10] text = text attribute: CharField. Use CharField when ou want to store a small
# amount of text, such as name, title, city, etc. Max length tells Django
# how much space to reserve in the database.

# [11] date_added = DateTimeField records date and time. auto_now_add=True tells
# Django to automatically set this attribute to current date/time when
# new topic is created.

# [14] __str__: returns the string stored in the text attribute.

# [19] Entry class inherits from Django's base Model class

# [22] First attr, topic, is a ForeignKey instance. FOREIGN KEY is a database
# term; a reference to another record in the database. This is the code
# that connects each entry to a specific topic. Each topic is assigned
# a key or ID when created.
#
# The on_delete=models.CASCADE tells Django that, whenever a topic is deleted,
# all entries associated with that topic should also be deleted (cascading delete).

# [23] Next attr, text, is an instance of TextField. date_added attr allows us to
# present entries in the order in which they were created and place a timestamp

# [26] We nest Meta inside Entry. This class holds extra information for managing
# a model. Here, it allows us to set a special attribute telling Django to use
# 'Entries' when it needs to refer to more than one entry.

# [29] __str__() tells Django which info to show when it refers to individual
# entries. We tell it just to use the first 50 chars.

# [2] import the User model from django.contrib.auth - This is for granting
# access only to logged in user for restricted pages like his topics

# [12] add an  owner field to Topic , which establishes a foreign key
# relationship to the User  model. If a user is deleted, all the topics
# associated with that user will be deleted as well.