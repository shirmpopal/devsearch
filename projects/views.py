from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm 
from .utils import search_projects

def projects(request):
  projects, search_query = search_projects(request)

  context = {
    'projects': projects,
    'search_query': search_query,
  }
  return render(request, 'projects/projects.html', context)

def project(request, pk):
  project = Project.objects.get(id=pk)
  context = {
    'project': project,
  }
  return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def add_project(request):
  profile = request.user.profile
  form = ProjectForm

  if request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.owner = profile
      project.save()
      return redirect('users-account')

  context = {
    'form': form,
  }
  return render(request, 'projects/project-form.html', context)

@login_required(login_url='login')
def update_project(request, pk):
  profile = request.user.profile
  project = profile.project_set.get(id=pk)
  form = ProjectForm(instance=project)

  if request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES, instance=project)
    if form.is_valid():
      form.save()
      return redirect('users-account')

  context = {
    'form': form,
  }
  return render(request, 'projects/project-form.html', context)

@login_required(login_url='login')
def delete_project(request, pk):
  profile = request.user.profile
  project = profile.project_set.get(id=pk)
  
  if request.method == 'POST':
    project.delete()
    return redirect('users-account')

  context = {
    'object': project 
  }
  return render(request, 'delete_template.html', context)