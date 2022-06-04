from django.urls import path
from . import views

app_name = 'api/rooms'


urlpatterns = [
    path('events/<str:placeName>/<str:date>/', views.AvailableBookingEventsByMonth.as_view()),

    path('setting/place/', views.PlacesListCreateAPI.as_view()),
    path('setting/place/<str:placeName>/', views.PlacesDestroyAPI.as_view()),

    path('setting/fixedtimetable/', views.FixedTimeTableListCreateAPI.as_view()),
    path('setting/fixedtimetable/<str:placeName>/', views.FixedTimeTableByPlaceAPI.as_view()),

    path('', views.RoomBookingListCreateAPI.as_view()),
    path('<int:id>/', views.RoomBookingDestroyAPI.as_view()),
    path('<str:placeName>/<str:date>/', views.RoomBookingsByDateAPI.as_view()),
]