from django.shortcuts import render


# Example 1 - variable


def learn_django(req):
    return render(req, "course/django.html", context={"name": "Django"})


# Create your views here.
