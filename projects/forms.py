from tkinter import Widget
from django.forms import ModelForm 
from .models import Project, Review
from django import forms 

class ProjectForm(ModelForm):
  class Meta:
    model = Project 
    fields = [
      'title',
      'description',
      'featured_image',
      'demo_link',
      'source_link',
      'tags',
    ]
    widgets = {
      'tags': forms.CheckboxSelectMultiple(),
    }

  def __init__(self, *args, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['value', 'body']
    labels = {
      'value': 'Place your vote',
      'body': 'Add a comment with your vote',
    }

  def __init__(self, *args, **kwargs):
    super(ReviewForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({'class': 'input'})