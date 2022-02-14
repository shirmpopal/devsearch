from unicodedata import name
from django.urls import path 
from . import views 

urlpatterns = [ 
  path('login', views.login_user, name='login'),
  path('logout', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  path('', views.profiles, name='users-profiles'),
  path('profile<str:pk>', views.profile, name='users-profile'),
  path('account', views.user_account, name='users-account'),
  path('edit-account', views.edit_account, name='users-edit-account'),
  path('add-skill', views.create_skill, name='users-create-skill'),
  path('update-skill<str:pk>', views.update_skill, name='users-update-skill'),
  path('delete-dkill<str:pk>', views.delete_skill, name='users-delete-skill'),
]