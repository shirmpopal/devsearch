from django.shortcuts import render
from .models import Project 

def projects(request):
  projects = Project.objects.all()
  context = {
    'projects': projects,
  }
  return render(request, 'projects/projects.html', context)