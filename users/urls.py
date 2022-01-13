from django.urls import path 
from . import views 

urlpatterns = [ 
  path('', views.profiles, name='users-profiles'),
  path('profile<str:pk>', views.profile, name='users-profile'),
]