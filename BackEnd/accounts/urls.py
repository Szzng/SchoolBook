from django.urls import path
from .views import RegisterView, LoginView

app_name = 'api/accounts'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/<str:pk>/', LoginView.as_view()),
]
