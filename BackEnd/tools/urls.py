from django.urls import path
from . import views

app_name = 'api/tools'

urlpatterns = [
    path('setting/', views.ToolListCreate.as_view()),
    path('setting/destroy/', views.ToolDestroy.as_view()),

    path('', views.ToolBookingListCreate.as_view()),
    path('<int:bookingId>/', views.ToolBookingDestroy.as_view()),
    path('<str:tool>/<str:date>/', views.ToolBookingRetrieve.as_view()),
    path('left/<str:tool>/<str:date>/', views.AvailableLeftRetrieve.as_view()),
]
