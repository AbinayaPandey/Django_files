from django.urls import path
from core.views import home

urlpatterns = [path("", home), path("home/", home)]  # For going to 8000
