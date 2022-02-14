from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomeUserCreationForm, ProfileForm, SkillForm


def login_user(request):
  if request.user.is_authenticated:
    return redirect('users-profiles')
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist!')
    else:
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        messages.success(request, 'Logged in successfully!')
        return redirect('users-profiles')
      else:
        messages.error(request, 'Username or password incorrect!')

  return render(request, 'users/login-register.html')

def logout_user(request):
  logout(request)
  messages.success(request, 'Logged out!')
  return redirect('login')

def register_user(request):
  page = 'register'
  form = CustomeUserCreationForm()

  if request.method == 'POST':
    form = CustomeUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      messages.success(request, 'Account registered!')
      login(request, user)
      return redirect('users-edit-account')
    else:
      messages.error(request, 'Error occurred during regitration!')

  context = {
    'page': page,
    'form': form,
  }
  return render(request, 'users/login-register.html', context)

def profiles(request):
  profiles = Profile.objects.all()
  context = {
    'profiles': profiles,
  }
  return render(request, "users/profiles.html", context)

def profile(request, pk):
  profile = Profile.objects.get(id=pk)
  top_skills = profile.skill_set.exclude(description="")
  other_skills = profile.skill_set.filter(description="")
  context ={
    'profile': profile,
    'top_skills': top_skills,
    'other_skills': other_skills,
  }
  return render(request, 'users/profile.html', context)

@login_required(login_url="login")
def user_account(request):
  profile = request.user.profile
  skills = profile.skill_set.all()
  projects = profile.project_set.all()
  context = {
    'profile': profile,
    'skills': skills,
    'projects': projects
  }
  return render(request, 'users/account.html', context)

@login_required(login_url='login')
def edit_account(request):
  profile = request.user.profile
  form = ProfileForm(instance=profile)

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile ) 
    if form.is_valid():
      form.save()
      return redirect('users-account')
  context = {
    'form': form,
  }
  return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def create_skill(request):
  profile = request.user.profile
  form = SkillForm
  
  if request.method == 'POST':
    form = SkillForm(request.POST)
    if form.is_valid():
      skill = form.save(commit=False)
      skill.owner = profile
      skill.save()
      return redirect('users-account')

  context = {
    'form': form,
  }
  return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def update_skill(request, pk):
  profile = request.user.profile
  skill = profile.skill_set.get(id=pk)
  form = SkillForm(instance=skill)

  if request.method == 'POST':
    form = SkillForm(request.POST, instance=skill)
    if form.is_valid():
      form.save()
      return redirect('users-account')

  context = {
    'form': form,
  }
  return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def delete_skill(request, pk):
  profile = request.user.profile
  skill = profile.skill_set.get(id=pk)
  if request.method == 'POST':
    skill.delete()
    return redirect('users-account')
  context = {
    'object': skill,
  }
  return render(request, 'delete_template.html', context)