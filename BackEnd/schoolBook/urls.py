from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tablets/', include('tablets.urls')),
    path('api/rooms/', include('rooms.urls')),
]
