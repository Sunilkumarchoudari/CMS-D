from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('', views.students, name='students'),
    path('', views.testing, name='testing'),
]
