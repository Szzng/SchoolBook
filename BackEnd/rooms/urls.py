from django.urls import path
from . import views

app_name = 'api/rooms'



urlpatterns = [
    path('', views.RoomBookingListCreateAPI.as_view()),
    path('<int:id>/', views.RoomBookingDestroyAPI.as_view()),
    path('<str:placeName>/<str:date>/', views.RoomBookingsByDateAPI.as_view()),
    path('events/<str:placeName>/<str:date>/', views.AvailableBookingEventsByMonth.as_view()),

]