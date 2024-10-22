
from django.urls import path
from .views import login_view, password_lost,User_registeration  # Replace with your actual view

urlpatterns = [
    path('login/', login_view, name='login'), 
    path('password-recovery/', password_lost, name='password-recovery'), 
    path('register/', User_registeration, name='registration')
]

