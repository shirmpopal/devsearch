from tkinter import Widget
from django.forms import ModelForm 
from .models import Project 
from django import forms 

class ProjectForm(ModelForm):
  class Meta:
    model = Project 
    fields = [
      'owner',
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
