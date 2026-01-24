from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile  

def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            em = form.cleaned_data["email"]
            pw = form.cleaned_data["password"]

            # Saves Data Into Database
            user = Profile(name=nm, email=em, password=pw)
            user.save()

            # # Update Data Into Database
            # user = Profile(id=1, name=nm, email=em, password=pw)
            # user.save()

            # # Delete Data from Database
            # user = Profile(id=1)
            # user.delete()

            return HttpResponseRedirect("/student/success/")
    else:
        form = Registration()
    return render(request, "student/register.html", {"form": form})


def reg_success(request):
    return render(request, "student/success.html")


# Create your views here.
