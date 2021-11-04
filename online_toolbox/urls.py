
from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('download_file', views.download_file, name='download_file'),
]
