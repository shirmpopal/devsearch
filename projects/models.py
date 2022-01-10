from django.db import models
from users.models import Profile 
import uuid

class Project(models.Model):
  owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  # featured_image = models.ImageField()
  demo_link = models.CharField(max_length=200, null=True, blank=True)
  source_link = models.CharField(max_length=200, null=True, blank=True)
  vote_count = models.IntegerField(default=0, null=True, blank=True)
  vote_ratio = models.IntegerField(default=0, null=True, blank=True)
  tags = models.ManyToManyField('Tag', blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.title)

class Review(models.Model):
  VALUE_TYPE = (
    ('up', 'Up_vote'),
    ('down', 'Down_vote')
  )
  project = models.OneToOneField(Project, on_delete=models.CASCADE)
  # owner = 
  body = models.TextField(null=True, blank=True)
  value = models.CharField(max_length=200, choices=VALUE_TYPE)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.value)

class Tag(models.Model):
  name = models.CharField(max_length=200)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)

