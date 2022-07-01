from django.urls import path
from . import views

app_name = 'api/rooms'

urlpatterns = [
    path('setting/', views.RoomListCreate.as_view()),
    path('setting/destroy/', views.RoomDestroy.as_view()),

    path('setting/timetable/', views.TimetableCreate.as_view()),
    path('setting/timetable/<str:room>/', views.TimetableRetrieve.as_view()),

    path('events/<str:room>/<str:date>/', views.AvailableEventByMonthRetrieve.as_view()),

    path('', views.RoomBookingCreate.as_view()),
    path('<int:bookingId>/', views.RoomBookingDestroy.as_view()),
    path('<str:room>/<str:date>/', views.RoomBookingRetrieve.as_view()),
]
