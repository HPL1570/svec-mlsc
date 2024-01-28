from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('team', team, name='team'),
    path('event', event, name='event'),
    path('blog', blog, name='blog'),
    path('project', project, name='project'),
]