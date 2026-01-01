from django.urls import path
from course.views import learn_python, learn_django

urlpatterns = [
    path("dj/", learn_django, name="django"),
    path("py/", learn_python, name="python"),
]
