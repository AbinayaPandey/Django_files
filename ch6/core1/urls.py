from django.urls import path
from core1.views import home

urlpatterns = [path("", home), 
    path("home/", home, name="home")]  # For going to 8000
