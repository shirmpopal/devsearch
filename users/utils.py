from turtle import right
from django.db.models import Q
from .models import Profile, Skill 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search_profiles(request):
  search_query = ''

  if request.GET.get('search_query'):
    search_query = request.GET.get('search_query')

  skills = Skill.objects.filter(name__icontains=search_query)

  profiles = Profile.objects.distinct().filter(
    Q(name__icontains=search_query) |
    Q(headline__icontains=search_query) |
    Q(skill__in=skills))

  return profiles, search_query

def paginate_profiles(request, profiles, profiles_per_page):
  page = request.GET.get('page')
  paginator = Paginator(profiles, profiles_per_page)

  try:
    profiles = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    profiles = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    profiles = paginator.page(page)

  left_index = (int(page) - 1)
  if left_index < 1:
    left_index = 1
  
  right_index = (int(page) + 2)
  if right_index > paginator.num_pages:
    right_index = paginator.num_pages

  custome_range = range(left_index, right_index)

  return profiles, custome_range

