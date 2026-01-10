from django.shortcuts import render
from student.forms import Registration


def registration(req):
    fm = Registration(auto_id=True)
    return render(req, "student/registration.html", {"form": fm})
