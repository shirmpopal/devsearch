from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from .forms import CustomeUserCreationForm
from django.contrib import messages
from .models import Profile

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
      return redirect('users-profiles')
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