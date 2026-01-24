from django.urls import path
from student.views import register, reg_success

urlpatterns = [
    path('register/', register, name='register'),
    path('success/', reg_success, name='success')
]
# This may be the second file that runs as the first urls.py INCLUDES this file. 