from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/tablets'

router = DefaultRouter()
router.register(r'destroy', views.DestroyBookingViewSet, basename='Destroy')
router.register(r'', views.BookedTabletsByDateViewSet, basename='Tablets')

urlpatterns = [
    path('', include(router.urls)),
]