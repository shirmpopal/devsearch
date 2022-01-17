from django.urls import path 
from . import views 

urlpatterns = [ 
  path('', views.projects, name='projects-projects'),
  path('project/<str:pk>', views.project, name='projects-single-project'),
]