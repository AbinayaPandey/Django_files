from django.shortcuts import render


def learn_django(req):
    return render(req, "course/django.html")


def learn_fastapi(req):
    return render(req, "course/fastapi.html")


# Create your views here.
