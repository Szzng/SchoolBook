from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/tablets'


urlpatterns = [
    path('', views.BookedTabletsListCreateAPI.as_view()),
    path('<int:id>/', views.BookedTabletsDestroyAPI.as_view()),
    path('<str:placeName>/<str:date>/', views.BookedTabletsByDateAPI.as_view()),
    path('left/<str:placeName>/<str:date>/', views.LeftTabletsCountAPI.as_view()),
]