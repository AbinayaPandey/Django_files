from django.urls import path
from course.views import learn_django, learn_python

urlpatterns = [
    path("dj/", learn_django),  # For going to 8000.course/dj
    path("py/", learn_python),  # For going to 8000.course/py
]
