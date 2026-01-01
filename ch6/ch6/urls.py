from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # This is the Defult line of code
    path(
        "", include("core1.urls")
    ),  # This is for the home || when 8000 path ma jada. Core ko code run hunxa
    path(
        "course/", include("course.urls")
    ),  # This is for the corse app. For going to 8000.course
]
