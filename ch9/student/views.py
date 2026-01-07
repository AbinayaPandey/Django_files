from django.shortcuts import render
from student.models import profile


def all_data(req):
    all_students = profile.objects.all()
    print(all_students)
    return render(req, "student/all.html", {"students": all_students})


def single_data(req):
    student = profile.objects.get(pk=1)
    print(student)
    return render(req, "student/single.html", {"student": student})


# Ya ko students html file ma janxa ani for loop ma use hunxa.
