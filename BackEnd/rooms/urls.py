from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/rooms'

router = DefaultRouter()
router.register(r'', views.BookedRoomByDateViewSet, basename='Rooms')
router.register(r'destroy', views.DestroyBookingViewSet, basename='Destroy')


urlpatterns = [
    path('', include(router.urls)),
]