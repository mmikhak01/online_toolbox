from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('online_toolbox/', include('online_toolbox.urls')),
    path('', include('wmst.urls')),
    path('admin/', admin.site.urls),
]
