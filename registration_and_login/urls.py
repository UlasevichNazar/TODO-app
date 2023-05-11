from django.contrib.auth.views import LogoutView
from django.urls import path

from registration_and_login.views import CustomLoginView, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('reg/', RegisterPage.as_view(), name='register'),
]