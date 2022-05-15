from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/tablets'

router = DefaultRouter()
# router.register(r'timetable', views.TimeTableViewSet, basename='TimeTable')
router.register(r'', views.TabletsViewSet, basename='Tablets')

urlpatterns = [
    path('', include(router.urls)),
]