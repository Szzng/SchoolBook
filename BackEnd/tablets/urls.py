from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/tablets'

router = DefaultRouter()
router.register(r'', views.BookedTabletsByDateViewSet, basename='Tablets')
router.register(r'left', views.LeftTabletsViewSet, basename='Tablets')
router.register(r'destroy', views.DestroyBookingViewSet, basename='Destroy')


urlpatterns = [
    path('', include(router.urls)),
]