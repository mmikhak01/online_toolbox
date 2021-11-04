from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.wmst , name='index'),
    path('wmst', views.wmst , name='wmst'),
    #path('new_note', views.new_note , name='new_note'),
]
