from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class CustomeUserCreationForm(UserCreationForm):
  class Meta:
    model = User 
    fields = ['first_name', 'email', 'username', 'password1', 'password2']
    labels = {
      'first_name': 'Name'
    }
  def __init__(self, *args, **kwargs):
      super(CustomeUserCreationForm, self).__init__(*args, **kwargs)
      for field in self.fields.values():
        field.widget.attrs.update({'class': 'input'})
