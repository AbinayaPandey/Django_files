from django.shortcuts import render


def learn_django(req):
    return render(
        req, "course/django.html"
    )  # When you type course.dj/ the url will direct it to
    # views and then the learn_django function will render


def learn_python(req):
    return render(req, "course/python.html")
