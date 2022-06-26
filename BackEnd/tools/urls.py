from django.urls import path
from . import views

app_name = 'api/tools'

urlpatterns = [
    path('setting/', views.ToolListCreate.as_view()),
    path('setting/<int:pk>/', views.ToolRetrieveUpdateDestroy.as_view()),

    path('', views.ToolBookingListCreate.as_view()),
    path('<int:bookingId>/', views.ToolBookingDestroy.as_view()),
    path('<int:toolId>/<str:date>/', views.ToolBookingRetrieve.as_view()),
    path('left/<int:toolId>/<str:date>/', views.AvailableLeftRetrieve.as_view()),
]
