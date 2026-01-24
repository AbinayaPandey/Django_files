from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        # print(form)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            print("Name:", name)
            print("Email:", email)
            print("Password:", password)
            
            return HttpResponseRedirect("/student/success/")
    
    else:
        form = Registration()
    return render(request, "student/register.html", {"form": form})

def reg_success(request):
    return render(request, "student/success.html")


# This is the third file running as this views.py declares the method specified in the 2nd urls.py file.
