from django.urls import path
from course.views import learn_django, learn_fastapi

urlpatterns = [
    path("learn_django/", learn_django),
    path("learn_fastapi/", learn_fastapi),
]
