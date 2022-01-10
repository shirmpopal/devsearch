from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import OneToOneField 
import uuid 

class Profile(models.Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=500, null=True, blank=True)
  username = models.CharField(max_length=200, null=True, blank=True)
  headline = models.TextField(null=True, blank=True)
  location = models.CharField(max_length=500, null=True, blank=True)
  # profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/", default='profiles/default.png')
  social_github = models.CharField(max_length=200, null=True, blank=True)
  social_twitter = models.CharField(max_length=200, null=True, blank=True)
  social_linkedin = models.CharField(max_length=200, null=True, blank=True)
  social_youtube = models.CharField(max_length=200, null=True, blank=True)
  social_website = models.CharField(max_length=200, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.user.username)


class Skill(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)

