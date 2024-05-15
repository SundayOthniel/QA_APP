from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('user-registration/<int:id>', views.register, name='user_registration'),
    path('user-login', views.user_login, name='user-login'),
]