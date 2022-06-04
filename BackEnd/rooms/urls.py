from django.urls import path
from . import views

app_name = 'api/rooms'


urlpatterns = [
    path('events/<str:placeName>/<str:date>/', views.AvailableBookingEventsByMonth.as_view()),

    path('setting/', views.PlacesListCreateAPI.as_view()),
    path('setting/destroy/', views.PlacesDestroyAPI.as_view()),

    path('setting/timetable/', views.FixedTimeTableListCreateAPI.as_view()),
    path('setting/timetable/<str:placeName>/', views.FixedTimeTableByPlaceAPI.as_view()),

    path('', views.RoomBookingListCreateAPI.as_view()),
    path('<int:id>/', views.RoomBookingDestroyAPI.as_view()),
    path('<str:placeName>/<str:date>/', views.RoomBookingsByDateAPI.as_view()),
]