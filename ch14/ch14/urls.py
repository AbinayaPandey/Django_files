from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student/", include('student.urls'))
]
# So this is the file that runs first. When you enter anything after user 8000. This will include all of the urls of inside
# of the urls.py of the student folder