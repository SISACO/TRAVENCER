
from django.urls import path
from .views import login_view  # Replace with your actual view

urlpatterns = [
    path('login/', login_view, name='login'),  # Name of the URL
]

