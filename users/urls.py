from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]