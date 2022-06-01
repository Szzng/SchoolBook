from django.urls import path
from . import views

app_name = 'api/rooms'


urlpatterns = [
    path('setting/place/', views.SetPlacesListCreateAPI.as_view()),
    path('setting/place/<str:placeName>/', views.SetPlacesDestroyAPI.as_view()),

    path('setting/fixedtimetable/', views.SetFixedTimeTableListCreateAPI.as_view()),
    path('setting/fixedtimetable/<str:placeName>/', views.SetFixedTimeTableByPlaceAPI.as_view()),

    path('', views.RoomBookingListCreateAPI.as_view()),
    path('<int:id>/', views.RoomBookingDestroyAPI.as_view()),
    path('<str:placeName>/<str:date>/', views.RoomBookingsByDateAPI.as_view()),

    path('events/<str:placeName>/<str:date>/', views.AvailableBookingEventsByMonth.as_view()),
]