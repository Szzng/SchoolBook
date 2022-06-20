from django.urls import path
from .views import RegisterView, LoginView, LogoutView, SchoolDetail

app_name = 'api/accounts'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('detail/', SchoolDetail.as_view()),
]
