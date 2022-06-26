from django.urls import path
from . import views

app_name = 'api/rooms'

urlpatterns = [
    path('setting/', views.RoomListCreate.as_view()),
    path('setting/destroy/', views.RoomDestroy.as_view()),

    path('setting/timetable/', views.TimetableListCreate.as_view()),
    path('setting/timetable/<int:roomId>/', views.TimetableRetrieve.as_view()),

    path('events/<int:roomId>/<str:date>/', views.AvailableEventByMonthRetrieve.as_view()),

    path('', views.RoomBookingListCreate.as_view()),
    path('<int:bookingId>/', views.RoomBookingDestroy.as_view()),
    path('<int:roomId>/<str:date>/', views.RoomBookingRetrieve.as_view()),
]
