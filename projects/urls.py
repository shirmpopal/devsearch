from unicodedata import name
from django.urls import path 
from . import views 

urlpatterns = [ 
  path('', views.projects, name='projects-projects'),
  path('project/<str:pk>/', views.project, name='projects-single-project'),
  path('add-project/', views.add_project, name='projects-add-project'),
  path('update-project/<str:pk>/', views.update_project, name='projects-update-project'),
  path('delete-project/<str:pk>/', views.delete_project, name='projects-delete-project')
]