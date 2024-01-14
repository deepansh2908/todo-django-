# model forms in django are simply form representation of a model 
from django import forms
from django.forms import ModelForm
from .models import *

# now creating a model form for the Task model
class TaskForm(ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'