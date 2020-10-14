from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): # 1
	class Meta:
		model = Topic # 2
		fields = ['text']
		labels = {'text': ''} # 3

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''} # 4
		widgets = {'text': forms.Textarea(attrs={'cols': 80})} # 5

## 1. We first import the forms module and the model we’ll work with, called
## Topic. We define a class called TopicForm , which inherits from forms.ModelForm
## The simplest version of a ModelForm consists of a nested Meta class tell-
## ing Django which model to base the form on and which fields to include in
## the form.

## 2. We build a form from the Topic model and include only the
## text field.

## 3. This tells Django not to generate a label for the text field

## 4. We have given the field 'text' a blank label. Edit: removed 'text', was redundant

## 5. We include the widgets attribute. A widget is an HTML form ele-
## ment, such as a single-line text box, multi-line text area, or drop-down list.
## By including the widgets attribute, you can override Django’s default widget
## choices. By telling Django to use a forms.Textarea element, we’re customizing
## the input widget for the field 'text' so the text area will be 80 columns wide
## instead of the default 40. This gives users enough room to write a meaning-
## ful entry.



