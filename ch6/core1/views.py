from django.shortcuts import render


def home(req):
    return render(req, "core1/home.html")
