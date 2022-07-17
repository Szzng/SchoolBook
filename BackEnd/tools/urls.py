from django.urls import path
from . import views

app_name = 'api/tools'

urlpatterns = [
    path('setting/', views.ToolListCreate.as_view()),
    path('setting/<str:name>/', views.ToolRetrieveUpdateDestroy.as_view()),

    path('', views.ToolBookingCreate.as_view()),
    path('<int:bookingId>/', views.ToolBookingDestroy.as_view()),
    path('<str:tool>/<str:date>/', views.ToolBookingsByDate.as_view()),
    path('left/<str:tool>/<str:date>/', views.LeftQuantityRetrieve.as_view()),
]
