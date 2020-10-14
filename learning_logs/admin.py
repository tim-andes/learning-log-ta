from django.contrib import admin

# 1.
from .models import Topic, Entry

# Register your models here.
# 2.
admin.site.register(Topic)

# 1. The dot in front of models tells django to look in the same directory
# as models.py

# 2. This code tells Django to manage our model through the admin site

# added ', Entry' to import line
admin.site.register(Entry)
